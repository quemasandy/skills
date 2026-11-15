# Operación práctica en GoHighLevel / Running X

## Estructura de página
- En Websites/Funnels: Section → Row → Column → Custom Code.
- Para fondos full-screen ajustar todos los padres a 100%/full width, márgenes y padding 0 según diseño.
- CSS del sitio debe estar bajo un selector raíz único; evitar `body`, `html` y reglas globales que interfieran con el builder.
- Contenido legible: `max-width` 1100–1400px interno, aun cuando el fondo llegue a los bordes.
- Testear 1440, 390 y ancho intermedio, sin desbordamiento horizontal.

## Calendarios
- Preferir el elemento Calendar si se puede editar nativamente.
- Al embeber usar URL permanente del widget `/widget/booking/<id>`, un iframe visible, altura suficiente y script de GHL solo una vez si corresponde.
- Si no renderiza: probar URL directa, tamaño de iframe, lazy loading, JS del builder y página pública.
- Si muestra “No slot available”: revisar usuario, zona horaria, disponibilidad, anticipación, rango de fechas, buffers, límites y conflictos externos.
- `Intervalo de reunión` = frecuencia de inicios; `Duración` = minutos de llamada.
- `Aviso mínimo` = ventana de anticipación; `Intervalo de fechas` = cuántos días hacia delante permite reservar.

## Formularios y CRM
- Nombre y email de trabajo; empresa, servicio y problema en función del objetivo. Teléfono opcional si no es imprescindible.
- Mensaje de agradecimiento en idioma de la página, sin prometer confirmación antes de que exista.
- Revisar envío en Form Submissions y contacto en CRM; pipeline y follow-up pueden requerir Workflow.
- Diferenciar alertas internas, respuesta al cliente, confirmación, cancelación y recordatorio.
- Evitar doble envío entre formulario, notificaciones del calendario y Workflow.
- Consentimiento marketing separado y voluntario; política de privacidad publicada.

## Dominio
- Guardar captura/exportación de DNS antes de cambiar nada.
- A/ALIAS/CNAME de la web podrían entrar en conflicto con el alojamiento anterior.
- Conservar MX, TXT SPF, DKIM y DMARC si siguen en uso.
- Confirmar targets exactamente en GHL y proveedor DNS, no confiar en IPs históricas.
- Verificar dominio apex, www, HTTPS y ruta de envío/recepción de correo.

## Publicación
Probar en preview y URL pública, no solamente editor; reserva completa en widget real; correos correctos; apariencia móvil; enlaces CTA; metadata SEO; privacidad y seguridad.
