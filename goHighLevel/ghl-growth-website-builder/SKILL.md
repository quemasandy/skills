---
name: ghl-growth-website-builder
description: Diseña, construye y valida sitios y landing pages orientados a conversión en GoHighLevel (GHL / Running X / Ronin X), con HTML/CSS, formularios, calendarios, CRM, automatizaciones y dominios. Úsala para crear, mejorar o reparar sitios GHL.
---

# GHL Growth Website Builder

## Objetivo
Crear sitios profesionales que generen oportunidades reales. Recorrido: visita → oferta entendida → confianza → formulario o reserva → contacto/CRM → seguimiento → venta.

## Proceso obligatorio
1. Leer `references/lecciones-a10z.md`, `references/operacion-ghl.md` y `references/qa.md`.
2. Definir audiencia, problema, oferta, prueba verificable, CTA y criterio de éxito. Si faltan detalles no críticos, declarar supuestos y avanzar.
3. Elegir arquitectura: one-page para MVP enfocado; multipágina para contenidos/SEO; landing independiente para campañas o públicos específicos.
4. Crear identidad gráfica propia por cliente (tokens de colores, fuentes, grid y espaciado). **No copiar automáticamente A10Z**.
5. Copy: explicar en los primeros segundos qué se hace, para quién y cómo ayuda. No inventar testimonios, métricas, clientes, precios ni resultados.
6. Construir componentes accesibles y responsive, preferentemente nativos de GHL para formularios y calendarios. HTML personalizado solo si aporta control visual. Mantener CSS aislado mediante un ID raíz único.
7. Diseño full bleed: permitir fondo de ancho completo y contenido con max-width centrado. En GHL revisar Section → Row → Column → Custom Code, eliminar padding externo no deseado, probar escritorio y móvil. Hero con min-height basado en `100svh` sin recortar contenido.
8. Calendario: usar URL permanente, no one-time link. Preferir componente Calendar nativo; si se integra iframe, definir altura visible y fallback, y cargar script de GHL una sola vez. Verificar horario directo y embed. Intervalo de slots, duración, aviso mínimo, rango, buffers y límites son parámetros distintos.
9. Formularios: etiquetas claras; mínimos campos; privacidad real; consentimiento promocional separado y opcional; no textos placeholder legales; mensaje enviado ≠ reunión confirmada.
10. Automatizaciones: conservar un único flujo responsable por evento y evitar duplicaciones de correos. Verificar Envíos, Contactos, Conversaciones y Oportunidades.
11. DNS: consultar valores actuales pedidos por GHL, inventariar registros anteriores, cambiar solo A/ALIAS/CNAME web conflictivos. **Nunca eliminar indiscriminadamente MX, SPF, DKIM, DMARC o nameservers.** Validar HTTPS, www/raíz y envío/recepción.
12. QA: revisar `references/qa.md`. Diferenciar código generado, preview local y publicación realmente comprobada. No asegurar reservas o correos sin pruebas.

## Entregables
- HTML/CSS para Custom Code, sin doctype/html/body cuando sea un bloque integrado.
- Vista previa HTML independiente.
- Variables editables de identidad, copy y URLs.
- Guía de instalación y QA para GHL.
- Instrucciones de calendar, formulario y DNS solo cuando apliquen.

## Reparación de sitios
Inspeccionar el fallo concreto (contenedor GHL, CSS local, iframe/script, disponibilidad, CRM, DNS), proponer el parche mínimo reversible y volver a probar. No rediseñar todo si el fallo es puntual.

## Fuentes
- https://help.gohighlevel.com/support/solutions/articles/155000005428-getting-started-launch-a-website-from-blank
- https://help.gohighlevel.com/support/solutions/articles/48001155718-adjusting-availability-settings-for-individual-calendars
- https://help.gohighlevel.com/support/solutions/articles/48001153720
