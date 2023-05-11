---
title: Migré mi blog de Gastby a Astro con ayuda de ChatGPT
pubDate: 'May 11 2023'
tags:
- programacion
---

Acabo de migrar mi blog a [astro](https://astro.build/). Tenía ganas desde hace rato, la verdad es que [gatsby](https://github.com/jackbravo/gatsby-jackbravo) había caído de mis preferencias como plataforma para sitios estáticos desde hacía rato. Para un texto (en inglés) bastante completo al respecto, recomiendo este blog sobre [Gatsby vs Next](https://jaredpalmer.com/blog/gatsby-vs-nextjs) que es bastante bueno. El resumen es que:

- Necesitas aprender GraphQL, cuando GraphQL es una tecnología bastante compleja por sí sola
- Debuguear Gatsby es muy difícil, ya que tiene muchas capas como GraphQL, plugins, y una etapa de compilación que lanza errores confusos
- Los plugins y código que escribes en tu gatsby-node.js tiende a ser muy frágil, muchos plugins te piden agregar cosas al gatsby-node, que pueden parecer similares, pero no lo son en realidad, y terminas con un código gigante que no sabes muy bien cómo funciona. Actualizar gatsby luego se vuelve bastante complejo también

Yo sufrí todas ellas y el blog me sonó bastante acertado. Así que decidí buscar algo nuevo para actualizar mi blog, que tenía una versión de Gatsby de hace 5 años. En su momento mi blog fue migrado de un sitio de drupal a gatsby. En el código de mi blog en gatsby todavía está el [script](https://github.com/jackbravo/gatsby-jackbravo/blob/master/src/scripts/import_posts.js) que usé para convertir los posts de Drupal a archivos de markdown para gatsby. Así que ahora lo que hice fue escribir un nuevo [script](https://github.com/jackbravo/jackbravo.github.io/blob/main/import_blog.py), pero ayudado ahora por [ChatGPT](https://openai.com/blog/chatgpt) :-p.

En los [commits](https://github.com/jackbravo/jackbravo.github.io/commits/main/import_blog.py) de mi blog dejé record de la conversación en inglés que tuve con ChatGPT, que pongo aquí de manera resumida:

1. Crear el [script inicial](https://github.com/jackbravo/jackbravo.github.io/commit/6698a9f7b1edf5a1f8f7b9de439c51135ab4487a):

   > create a script that moves `index.md` files that are stored inside a `pages` folder, but rename the destination file to have the name of the containing folder

2. Pedir poder recibir la carpeta origen y destino desde la línea de comandos [como argumentos](https://github.com/jackbravo/jackbravo.github.io/commit/bd9d6190baa6e327a7ddc4fdfb196332f61431e5) cuando llamara al script

   > make the root directory a [parameter you get from the command line], as well as the destination directory for all the files

3. Luego [le pedí](https://github.com/jackbravo/jackbravo.github.io/commit/1bec4f32b2a8f18bf4f50967bf7fa96c62dc9713) que me permitiera modificar parte de los archivos, renombrando una variable en cada uno de ellos de `date` a `pubDate`, que era como lo usaba astro, y que me organizara mejor el código. Además de que cambiara la lógica a copiar los archivos en vez de moverlos, para poder correr el archivo varias veces mientras debugueaba.

   > - now, the markdown files we are moving have a frontmatter section with metadata. I would like to rename the `date` property in this section to `pubDate`
   >
   > - can this update of the frontmatter section be done in a separate function? Or how can we better organize the code?
   >
   > - and I just realized that we are moving the source files instead of just copying them, which is less destructive and allows easier testing of the script :-p

Con cada iteración pude ir probando y modificando el script. Creo que esto me ahorró varias horas de trabajo, para encontrar qué librerías usar, cómo funcionan, y ponerlo todo junto. 5 estrellas. Gracias ChatGPT!!!

El resultado final lo pueden ver [aquí](https://github.com/jackbravo/jackbravo.github.io/blob/main/import_blog.py).
