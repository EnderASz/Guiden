const premieres_wrapper: HTMLDivElement = document.querySelector(`article.premieres .wrapper`)!;
const premieres_container: HTMLDivElement = premieres_wrapper.querySelector(`.container`)!;
const premieres_roll: HTMLUListElement = premieres_container.querySelector('.roll')!;
const premieres_tiles: NodeListOf<HTMLLIElement> = premieres_wrapper.querySelectorAll(`.tile`)!

const news_article = document.querySelector(`article.news`)!;
const news_wrapper: HTMLDivElement = news_article.querySelector(`.wrapper`)!;
const news_container: HTMLDivElement = news_wrapper.querySelector(`.container`)!;
const news_roll: HTMLUListElement = news_container.querySelector('.roll')!;
const news_tiles: NodeListOf<HTMLLIElement> = news_wrapper.querySelectorAll(`.tile`)!

const left_btn_news = news_article.querySelector(`.btn.left`)!;
const right_btn_news = news_article.querySelector(`.btn.right`)!;
const left_btn_premieres = premieres_wrapper.querySelector(`.btn.left`)!;
const right_btn_premieres = premieres_wrapper.querySelector(`.btn.right`)!;

let current_news = 0;
let start_premiere = 0;

function get_width(element: HTMLElement): number {
    let rect = element.getBoundingClientRect()
    return rect.right - rect.left;
}

function update_news_appearance(): void {
    news_roll.style.transition = 'none';

    if(current_news>=news_tiles.length) current_news = 0;
    if(current_news<0) current_news = news_tiles.length - 1;

    const tile_width = get_width(news_container);

    news_tiles.forEach((tile) => {
        tile.style.width = `${tile_width}px`;
        const overlap: HTMLDivElement = tile.querySelector(`.overlap`)!;
        const banner: HTMLImageElement = tile.querySelector(`.banner`)!;
        overlap.style.maxWidth = `${get_width(banner)}px`;
    })

    const container_width = get_width(news_container);
    news_roll.style.left = `${-current_news * container_width}px`;
    news_roll.style.width = `${2 * news_tiles.length * tile_width}px`;

    news_roll.style.transition = '';
}

function update_premieres_appearance(move: number=0): void {
    premieres_roll.style.transition = 'none';

    const tile_width = get_width(premieres_tiles[0]);

    const container_width = get_width(premieres_container);

    let fit = Math.floor(container_width / tile_width);

    if(start_premiere + fit > premieres_tiles.length - fit)
        start_premiere = 0;
    if(premieres_tiles.length > fit) {
        var margin_size = (container_width - fit*tile_width) / (2*fit);
        for(let i = 0; i < Math.abs(move); i++) {
            if(move > 0) {
                start_premiere = Math.min(start_premiere + fit, premieres_tiles.length - fit);
            }
            if(move<0) {
                if(start_premiere == 0) {
                    start_premiere = premieres_tiles.length-fit;
                    continue;
                }
                if(start_premiere < fit) {
                    start_premiere = 0
                    continue;
                }
                start_premiere -= fit;
                continue;
            }
        }
    } else {
        var margin_size = (container_width - premieres_tiles.length*tile_width) / (2*premieres_tiles.length);
        start_premiere = 0;
    }

    premieres_tiles.forEach(tile => tile.style.margin = `0 ${margin_size}px`);

    premieres_roll.style.width = `${2 * premieres_tiles.length * (tile_width + 2*margin_size)}px`;
    premieres_roll.style.left = `${-start_premiere * (2*margin_size + tile_width)}px`;

    premieres_roll.style.transition = '';
}

window.addEventListener("load", () => {
    update_news_appearance();
    update_premieres_appearance();
})
window.addEventListener("resize", ()=>{update_premieres_appearance()});
window.addEventListener("resize", update_news_appearance);
left_btn_news.addEventListener("click", ()=>{
    current_news--;
    update_news_appearance();
})
right_btn_news.addEventListener("click", ()=>{
    current_news++;
    update_news_appearance();
})
left_btn_premieres.addEventListener("click", ()=>{
    update_premieres_appearance(-1);
})
right_btn_premieres.addEventListener("click", ()=>{
    update_premieres_appearance(1);
})
