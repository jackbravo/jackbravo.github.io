import rss from '@astrojs/rss';
import { getCollection, render } from 'astro:content';
import { SITE_TITLE, SITE_DESCRIPTION } from '../consts';
import sanitizeHtml from 'sanitize-html';

export async function GET(context) {
	const posts = await getCollection('blog');
	const items = await Promise.all(
		posts.map(async (post) => {
			const { Content } = await render(post);
			// Render the Astro component to a string for RSS content
			const html = sanitizeHtml(post.rendered?.html || '', {
				allowedTags: sanitizeHtml.defaults.allowedTags.concat(['img']),
			});
			return {
				title: post.data.title,
				pubDate: post.data.pubDate,
				description: post.data.description || '',
				link: `/${post.id.replace(/\.md$/, '')}/`,
				content: html,
			};
		})
	);
	return rss({
		title: SITE_TITLE,
		description: SITE_DESCRIPTION,
		site: context.site,
		items,
	});
}
