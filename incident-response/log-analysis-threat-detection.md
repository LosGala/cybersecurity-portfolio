# Análisis de Logs — Detección de Amenazas Internas y Compromiso de Cuenta

**Rol simulado:** Analista de Seguridad Junior  
**Herramientas utilizadas:** NotebookLM (IA asistida), análisis manual de logs  
**Escenario:** Revisión de actividad inusual en sistema corporativo — `system_activity_log_2025-07-30.txt`
**Fuente:** Google Cybersecurity Certificate — Módulo: Herramientas de IA para Seguridad

---

## Datos de Registro Analizados

```
TIMESTAMP            | USER          | SOURCE_IP        | EVENT_TYPE         | DETAILS
2025-07-30 08:00:15  | admin         | 192.168.1.1      | Login_Success      | User 'admin' logged in from internal network
2025-07-30 08:05:30  | John.Doe      | 192.168.1.5      | File_Access        | Opened: /documents/report_draft.docx
2025-07-30 08:10:45  | jane.smith    | 192.168.1.10     | Email_Sent         | To: allstaff@company.com, Subject: Important Update
2025-07-30 08:15:00  | guest         | 10.0.0.100       | Login_Failed       | User 'guest' attempted login from unknown IP (1 attempt)
2025-07-30 08:15:05  | guest         | 10.0.0.100       | Login_Failed       | User 'guest' attempted login (2 attempts)
2025-07-30 08:15:10  | guest         | 10.0.0.100       | Login_Failed       | User 'guest' attempted login (3 attempts)
2025-07-30 08:20:20  | John.Doe      | 192.168.1.5      | File_Access        | Copied: /finance/budget_2026_final.xlsx to /public_share
2025-07-30 08:25:35  | system        | N/A              | Service_Status     | Web server (Apache) is running.
2025-07-30 08:30:40  | admin         | 203.0.113.25     | Login_Success      | User 'admin' logged in from external IP (unusual location)
2025-07-30 08:35:50  | mary.jones    | 192.168.1.12     | File_Deletion      | Deleted: /personal/vacation_photos.jpg
2025-07-30 08:40:05  | system        | N/A              | Software_Update    | Antivirus definitions updated successfully
```

---

## Resumen Ejecutivo

Se analizaron 11 entradas de log de un día de operación. Se identificaron **tres hallazgos de seguridad** que requieren atención:

| # | Hallazgo | Severidad |
|---|---|---|
| 1 | Posible exfiltración de datos — archivo financiero copiado a carpeta pública | 🔴 Crítico |
| 2 | Admin autenticado desde IP externa no habitual | 🟠 Alto |
| 3 | Intentos de fuerza bruta contra cuenta `guest` desde IP externa | 🟡 Medio |

---

## Pregunta 1 — Entrada de Registro Más Sospechosa

> ¿Qué entrada de registro es la más sospechosa y probablemente requeriría una escalada inmediata?

**Respuesta:**

| Fecha/Hora | Usuario | IP | Evento | Detalle |
|---|---|---|---|---|
| 2025-07-30 08:20:20 | John.Doe | 192.168.1.5 | File_Access | Copiado: `/finance/budget_2026_final.xlsx` a `/public_share` |

**Análisis:** Un archivo de presupuesto financiero con información sensible del próximo año fiscal fue copiado a un directorio de acceso público. Esto constituye una **potencial exfiltración de datos**, ya sea por:

- Un empleado malintencionado (amenaza interna)
- Una cuenta comprometida cuyas credenciales fueron robadas
- Error humano con graves consecuencias

**¿Por qué escalar inmediatamente?**
- Los archivos financieros son datos altamente sensibles y regulados.
- El directorio `/public_share` implica acceso no restringido.
- La exposición puede generar pérdidas financieras, daño reputacional y consecuencias legales.

---

## Pregunta 2 — Correlación de Eventos (Posible Compromiso)

> ¿Qué dos entradas de registro separadas, cuando se combinan, podrían indicar un posible compromiso de cuenta o una amenaza interna maliciosa?

**Respuesta:** La combinación del **inicio de sesión de admin desde IP externa (203.0.113.25)** y la **copia del archivo financiero por John.Doe**.

| Hora | Evento | Usuario | IP | Detalle |
|---|---|---|---|---|
| 08:20:20 | File_Access (Copy) | John.Doe | 192.168.1.5 | `budget_2026_final.xlsx` → `/public_share` |
| 08:30:40 | Login_Success | admin | **203.0.113.25** | IP externa — ubicación inusual |

**Análisis de correlación:**

1. El admin inició sesión desde la red interna (`192.168.1.1`) a las 08:00:15 — comportamiento normal.
2. A las 08:30:40, el mismo usuario `admin` inició sesión desde `203.0.113.25`, una IP externa — **altamente anómalo**.
3. Diez minutos antes (08:20:20), John.Doe realizó una copia sospechosa de un archivo financiero.

**Escenarios posibles:**
- Un atacante comprometió la cuenta de `admin` y luego usó ese acceso para robar datos a través de la sesión de John.Doe.
- John.Doe y admin están trabajando juntos (colusión interna).
- El login externo de admin y la copia de John.Doe son incidentes independientes pero igualmente graves.

**Recomendación:** Ambos eventos deben investigarse como parte de un mismo incidente hasta que se demuestre lo contrario.

---

## Pregunta 3 — Intentos de Inicio de Sesión Fallidos

> El registro muestra varios intentos fallidos de inicio de sesión desde una dirección IP específica. ¿Qué usuario y dirección IP estuvieron involucrados?

**Respuesta:**

| Usuario | Dirección IP |
|---|---|
| `invitado` (guest) | **10.0.0.100** |

**Detalle de los eventos:**

| Hora | Evento | Detalle |
|---|---|---|
| 08:15:00 | Login_Failed | Intento 1 — IP desconocida |
| 08:15:05 | Login_Failed | Intento 2 |
| 08:15:10 | Login_Failed | Intento 3 |

**Análisis:**
- La IP `10.0.0.100` no pertenece a la red interna (`192.168.1.0/24`), lo que sugiere un origen externo.
- Tres intentos fallidos consecutivos en 10 segundos indican un **ataque automatizado de fuerza bruta** o un atacante probando credenciales por defecto.
- La cuenta `guest` o `invitado` suele tener privilegios mínimos o nulos, pero es un vector común de reconocimiento.

---

## Tabla de Evaluación de Eventos

| Evento | Tipo | Evaluación | Justificación |
|---|---|---|---|
| Admin login 192.168.1.1 | Login_Success | ✅ Normal | IP interna, hora laboral |
| John.Doe abre report_draft.docx | File_Access | ✅ Normal | Actividad esperada |
| jane.smith envía email | Email_Sent | ✅ Normal | Comunicación interna |
| guest login failed ×3 | Login_Failed | ⚠️ Sospechoso | Fuerza bruta desde IP externa |
| John.Doe copia budget a public_share | File_Access | 🔴 Crítico | Exfiltración de datos |
| Apache running | Service_Status | ✅ Normal | Mantenimiento rutinario |
| Admin login 203.0.113.25 | Login_Success | 🔴 Crítico | Compromiso de cuenta |
| mary.jones borra vacation_photos.jpg | File_Deletion | ✅ Normal | Acción personal (bajo riesgo) |
| Antivirus update | Software_Update | ✅ Normal | Mantenimiento rutinario |

---

## Línea de Tiempo del Incidente

```
08:00:15 ── Admin login (192.168.1.1) ── Normal
08:05:30 ── John.Doe abre report_draft.docx ── Normal
08:10:45 ── jane.smith envía email ── Normal
08:15:00 ── guest login failed ×3 (10.0.0.100) ── ⚠️ Sospechoso
08:20:20 ── John.Doe COPIA budget a public_share ── 🔴 Crítico
08:25:35 ── Apache running ── Normal
08:30:40 ── admin login (203.0.113.25) ── 🔴 Crítico
08:35:50 ── mary.jones borra foto personal ── Normal
08:40:05 ── Antivirus update ── Normal
```

---

## Recomendaciones de Seguridad

### Inmediatas (24 horas)
1. **Bloquear IPs externas:** Agregar `203.0.113.25` y `10.0.0.100` a la lista de bloqueo del firewall.
2. **Restringir `/public_share`:** Revocar permisos de escritura/lectura públicos y auditar accesos.
3. **Forzar reseteo de contraseñas:** Admin y John.Doe — cambio obligatorio inmediato.
4. **Habilitar 2FA** en todas las cuentas privilegiadas.

### Corto Plazo (1 semana)
5. **Revisar sesiones activas** de admin y John.Doe para identificar accesos no autorizados.
6. **Implementar política de bloqueo de cuentas** tras 3-5 intentos fallidos (account lockout).
7. **Deshabilitar cuenta `guest`** si no tiene uso operativo justificado.

### Largo Plazo (1 mes)
8. **Implementar DLP (Data Loss Prevention)** para alertar sobre copias de datos sensibles a ubicaciones no autorizadas.
9. **Configurar alertas de geolocalización** para inicios de sesión desde IPs externas en cuentas privilegiadas.
10. **SIEM tuning:** Crear reglas de correlación para detectar patrones como "login externo + exfiltración" en ventanas de tiempo cortas.

---

## MITRE ATT&CK Mappings

| Técnica | ID | Descripción |
|---|---|---|
| Valid Accounts | T1078 | Uso de cuenta legítima (admin) desde IP externa |
| Exfiltration Over Web Service | T1567 | Copia de archivo a directorio público |
| Brute Force | T1110 | Múltiples intentos de login fallidos contra cuenta guest |
| Unauthorized Account Access | T1078.002 | Acceso no autorizado a cuenta de dominio |

---

## Lecciones Aprendidas

- **La IA (NotebookLM) es una herramienta de apoyo**, no de reemplazo. Ayuda a identificar patrones rápidamente, pero el análisis crítico humano es indispensable para correlacionar eventos y tomar decisiones.
- **Los logs más ruidosos no siempre son los más peligrosos.** Los 3 intentos fallidos de guest son sospechosos, pero la exfiltración silenciosa de John.Doe es más crítica.
- **La correlación temporal es clave.** Dos eventos separados por 10 minutos pueden ser la diferencia entre detectar un ataque a tiempo o sufrir una brecha consumada.

---

## Contacto

**Analista:** Mario Galarza  
**Email:** losgala911@gmail.com  
**LinkedIn:** [linkedin.com/in/losgala](https://linkedin.com/in/losgala)  
**Curso:** Google Cybersecurity Certificate — Módulo: Herramientas de IA para el Análisis de Seguridad
