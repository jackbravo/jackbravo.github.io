---
description: "Cómo actualicé mi blog personal con ayuda de agentes de IA autónomos — 14 PRs en un par de días, desde upgrade de Astro hasta dark mode y SEO."
title: Actualizando mi blog con ayuda de agentes de IA
pubDate: '2026-04-16'
tags:
- programacion
- ia
---

Hace unos años escribí sobre cómo [migré mi blog de Gatsby a Astro con ayuda de ChatGPT](/migracion-a-astro). La experiencia fue reveladora — le pedía cosas, copiaba el código, lo probaba, le pedía correcciones. Funcionó, pero era un proceso manual: yo era el que copiaba y pegaba.

Ahora las cosas avanzaron. Ya no necesito copiar nada. Los agentes de IA pueden ejecutar comandos, editar archivos, hacer commits, abrir pull requests — todo de manera autónoma. Recientemente tuve una operación en mi codo derecho, la necesidad es la madre de la invención, así que el dolor al usar el teclado fue una buena excusa para probar un agente tipo OpenClaw.

Decidí darle una revisada a mi blog, que ya tenía algún tiempo sin atención. Le pedí a mi agente que lo revisara y me diera una lista priorizada de mejoras. Me dio 15 puntos y me puse a trabajar en ellos.

## Upgrade de Astro 5 a 6

Lo primero fue actualizar Astro de la versión 5 a la 6. El agente investigó la guía de migración, identificó los cambios necesarios — migrar content collections a la nueva Content Layer API, cambiar `post.slug` por `post.id`, mover `config.ts` de lugar, actualizar el RSS endpoint — y abrió un PR con todo listo. Yo solo lo revisé y lo mergeé. Cambios en 11 archivos, y yo básicamente bajé y probé en local: "se ve bien, adelante."

## Optimización de imágenes

Después me hizo dar cuenta que tenía imágenes gigantes en el blog. Mi carpeta `public/` pesaba 55MB. Un PNG de una foto del bosque pesaba 17MB — era una foto de celular de 4032x3024 pixeles sin optimizar. El agente encontró 7 imágenes pesadas, las convirtió a WebP y redujo el tamaño a máximo 1200px de ancho. Resultado: de 55MB a 2.1MB. PR mergeado sin discusión.

## SEO y RSS

Varias mejoras fueron de SEO, y estas sí me parecieron más interesantes porque mostraron cómo el agente entiende el contexto. Resulta que ninguno de mis 75 posts tenía `description` en el frontmatter — o sea, cero. El agente generó una descripción para cada uno y abrió un PR con 59 archivos modificados. Luego se dio cuenta que mis páginas de tags (`/tags/drupal`, `/tags/git`) compartían todas el mismo título que la homepage. También arregló el RSS feed, que tenía URLs rotas (apuntaban a `/blog/<slug>/` cuando mis posts viven en `/<slug>/`) y no incluía el contenido de los posts. Y me encontró una imagen genérica de Astro como social image que reemplazó con mi logo de la gaceta.

## Dark mode

Una que sí discutimos más fue el dark mode. El agente quería agregarlo con CSS custom properties y `prefers-color-scheme`, respetando la preferencia del sistema operativo, sin toggle de JavaScript. Me pareció buena idea — yo no quería un botón de sol/luna, solo que funcionara. Lo interesante es que este PR chocó con otro que estaba haciendo al mismo tiempo (extraer CSS duplicado), y el agente tuvo que hacer un rebase y resolver conflictos. Yo aprobé el force push y listo. Al final el blog se ve bien en modo oscuro: fondo azul oscuro, texto claro, links azules. Y hasta los comentarios de giscus respetan el tema.

## No todo es vibe coding

Algo importante: todas las mejoras después del upgrade de Astro fueron sugeridas por el agente. Yo solo pedí que revisara el sitio y propusiera mejoras. De las 15 sugerencias que me dio, hicimos como 3/4. Y fue paso a paso — si hubiera pedido hacer todo de golpe creo que hubiera tardado más, fallado en alguna, o producido código más sucio. De hecho, cuando el agente estaba unificando el CSS y al mismo tiempo agregando el dark mode, hubo conflictos que complicaron las cosas. Paso a paso funciona mejor.

Sigo pensando que solo hacer vibe coding no es viable a largo plazo. Todavía se requiere que una persona revise lo que hace el agente, que tenga coherencia, que entienda el contexto. El agente es muy bueno ejecutando, pero la visión general sigue siendo humana.

## El agente detrás

Esta prueba la hice usando [Hermes](https://github.com/hugocore/hermes), un agente open source instalado en un VPS, con el [coding plan de Z.AI](https://z.ai/subscribe) y GLM 5.1 como motor principal de LLM. La conexión fue por Telegram — le mandaba mensajes como si fuera un chat normal y el agente iba clonando el repo, haciendo cambios, abriendo PRs en GitHub. Todo sin que yo abriera un editor de código. Localmente bajaba algunos cambios para comprobar que todo fuera bien.

Para codear cosas del trabajo sigo usando agentes más directos — [opencode](https://opencode.ai), [pi.dev](https://pi.dev) o GitHub Copilot — en lugar de algo tipo Hermes/OpenClaw. Cada herramienta tiene su momento. Pero para este tipo de revisión general de un proyecto personal, donde no necesito estar en el editor sino que quiero delegar y revisar, un agente conversacional funciona muy bien.

En total fueron 14 PRs mergeados en un par de días. Algunos los revisé a detalle, otros solo les di una hojeada rápida porque el cambio era obvio. No creo que yo hubiera hecho todo esto por mi cuenta — me hubiera dado flojera o no habría sabido por dónde empezar. Y me ahorra tiempo para las cosas que sí quiero hacer yo mismo, como escribir este post :-p.
