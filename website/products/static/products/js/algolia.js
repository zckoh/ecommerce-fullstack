const searchClient = algoliasearch(
    '9SXIDIVU1E',
    '2f579f9adf3af05e58b1859a5f182edb'
);

const search = instantsearch({
    indexName: 'Product',
    searchClient,
    routing: true,
});

search.addWidgets([
    instantsearch.widgets.configure({
        hitsPerPage: 6,
    }),
    instantsearch.widgets.searchBox({
        container: '#search-box',
        placeholder: 'Rechercher',
    }),
    instantsearch.widgets.refinementList({
        container: '#refinement-list',
        attribute: 'product_category',
        showMore: true,
        templates: {
          showMoreText: `
            {{#isShowingMore}}
              Montrer moins
            {{/isShowingMore}}
            {{^isShowingMore}}
              Montrer plus
            {{/isShowingMore}}
          `,
        },
    }),
    instantsearch.widgets.pagination({
      padding: '2',
      container: '#pagination',
    }),
    instantsearch.widgets.poweredBy({
      container: '#powered-by',
    }),
]);

// Hits
// Custom render function for search result (Hits)
const renderHits = (renderOptions, isFirstRender) => {
    const { hits, results, widgetParams } = renderOptions;

    if (hits === undefined || hits.length == 0) {
        if (document.getElementsByClassName("ais-SearchBox-input")[0].value) {
            widgetParams.container.innerHTML = `
                <p>Nous n'avons trouvé aucun résultat pour la recherche <em>"${document.getElementsByClassName("ais-SearchBox-input")[0].value}"</em></p>
            `;
        }
    } else {
        widgetParams.container.innerHTML = `
        <div class="row">
          ${hits
                .map(
                    item =>
            `<div class="col-md-4">
                <div class="card mb-4 box-shadow">
                    <a href="${item.slug}">
                      <img class="card-img-top product-thumbnail" src="https://storage.googleapis.com/tfnglun.appspot.com/${item.main_product_image}"
                          alt="${item.main_product_image}">
                    </a>
                    <div class="card-body product-body">
                        <a href="/products/${item.slug}" class="text-dark">
                            <h5 class="card-title">${item.product_name}</h5>
                        </a>
                        <p class="card-text">Référence: ${item.model_no}</p>
                        <a href="${item.slug}" class="btn btn-primary">Voir</a>
                    </div>
                </div>
            </div>`
                ).join('')}
        </div>
        `;
    }
};

// Create the custom widget for search result
const customHits = instantsearch.connectors.connectHits(renderHits);

// Instantiate the custom widget for search result
search.addWidgets([
    customHits({
        container: document.querySelector('#hits'),
    })
]);

search.start();
