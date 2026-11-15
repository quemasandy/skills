# Lecciones de A10Z (caso de referencia, no plantilla obligatoria)

## Estrategia comercial
A10Z AI Consulting pasó de un posicionamiento técnico abstracto a mensajes directos centrados en implementar IA, automatizar procesos, integrar APIs y modernizar plataformas. La función profesional FDE diferencia al consultor, mientras que AI Consulting describe un servicio comprensible. Una one-page con servicios, método, credenciales y agenda resolvió el MVP.

## Diseño
Estética Institutional Ink (azul noche, marfil, serif/sans) fue una elección particular. Para otros clientes usar paletas y layouts propios. El logo de calendario de 180×180 debe ser legible en pequeño.

## Incidentes y soluciones
- **Márgenes blancos**: contenedores Section → Row → Column → Custom Code imponían ancho/padding. Usar Full Width, 100%, padding 0, CSS local. Fondo full-bleed puede requerir `width:100vw;margin-left:calc(50% - 50vw)` siempre probado en móvil.
- **Hero corto**: usar `min-height:calc(100svh - alturaHeader)` y composición responsive.
- **Calendario invisible**: iframe sin altura o integración GHL problemática. Usar Calendar nativo cuando sea viable; si iframe, altura explícita, script oficial no duplicado y enlace alternativo. Probar widget directo y sitio público.
- **Calendario sin fechas**: rango de reserva = 1 día y anticipación mínima = 1 día provocaban ventana casi nula. Cambiar rango a 30 días permitió mostrar horarios. No confundir fallo de iframe con ausencia de slots.
- **Reglas de agenda**: intervalo entre puntos de inicio distinto de duración real; preparación y margen posterior bloquean tiempo; límite diario distinto de límite simultáneo.
- **Notificaciones**: solicitud pendiente no equivale a cita confirmada. Evitar correo nativo duplicado por workflow.
- **Porkbun y DNS**: ALIAS raíz y CNAME wildcard apuntaban a pixie.porkbun.com; se reemplazaron los registros web según GHL y se conservaron MX, SPF, DKIM y DMARC para no romper correo. Los valores de destino pueden variar: verificar en la plataforma actual.
- **Mailgun**: tener MX para mail.<dominio> no garantiza buzón tradicional; comprobar ruta de respuestas y Conversations.
- **Consentimiento**: no dejar [BUSINESS NAME] ni aceptar campañas por defecto.

## Parámetros históricos de A10Z
Duración 20 min; antelación mínima 1 día; rango 30 días; intervalos de inicio 1 hora; recomendación de buffers 15 min antes / 10 después; máximo 2 reservas/día y 1 simultánea. Son decisiones de A10Z, no predeterminados universales.
