const searchClient = algoliasearch(
    'N3F75G0U52',
    '35f5cf9db1a99f6024840246fdf8114c'
);

const search = instantsearch({
    indexName: 'products_index',
    searchClient,
    routing: true,
});

search.addWidgets([
    instantsearch.widgets.configure({
        hitsPerPage: 10,
    }),
    instantsearch.widgets.searchBox({
        container: '#search-box',
        placeholder: 'Search for products',
    }),
    instantsearch.widgets.refinementList({
        container: '#refinement-list',
        attribute: 'product_category',
    }),
]);

// Hits
// Custom render function for search result (Hits)
const renderHits = (renderOptions, isFirstRender) => {
    const { hits, results, widgetParams } = renderOptions;

    if (hits === undefined || hits.length == 0) {
        if (document.getElementsByClassName("ais-SearchBox-input")[0].value) {
            widgetParams.container.innerHTML = `
                <p>We didn't find any results for the search <em>"${document.getElementsByClassName("ais-SearchBox-input")[0].value}"</em></p>
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
                    <a href="${item.url_link}">
                      <img class="card-img-top product-thumbnail" src="/static/${item.product_image_path}"
                          alt="${item.product_image_path}">
                    </a>
                    <div class="card-body">
                        <a href="${item.url_link}" class="text-dark">
                            <h5 class="card-title">${item.product_name}</h5>
                        </a>
                        <p class="card-text">Model: ${item.model_no}</p>
                        <a href="${item.url_link}" class="btn btn-primary">View</a>
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

// Pagination
// Custom render function for Pagination widget
const renderPagination = (renderOptions, isFirstRender) => {
    const {
        pages,
        currentRefinement,
        nbPages,
        isFirstPage,
        isLastPage,
        refine,
        createURL,
    } = renderOptions;

    const container = document.querySelector('#pagination');

    container.innerHTML = `
      <ul class="pagination justify-content-center">
        ${
        !isFirstPage
            ? `
              <li class="page-item">
                <a class="page-link"
                  href="${createURL(0)}"
                  data-value="${0}"
                >
                  First
                </a>
              </li>
              <li class="page-item">
                <a class="page-link" aria-label="Previous"
                href="${createURL(currentRefinement - 1)}"
                  data-value="${currentRefinement - 1}"
                >
                <span aria-hidden="true">&laquo;</span>
                <span class="sr-only">Previous</span>
              </a>
              </li>
              `
            : ''
        }
        ${pages
            .map(
                page => `
              <li class="page-item">
                <a class="page-link"
                  href="${createURL(page)}"
                  data-value="${page}"
                  style="font-weight: ${currentRefinement === page ? 'bold' : ''}"
                >
                  ${page + 1}
                </a>
              </li>
            `
            )
            .join('')}
          ${
        !isLastPage
            ? `
                <li class="page-item">
                  <a class="page-link" aria-label="Next"
                    href="${createURL(currentRefinement + 1)}"
                    data-value="${currentRefinement + 1}"
                  >
                      <span aria-hidden="true">&raquo;</span>
                      <span class="sr-only">Next</span>
                </a>

                </li>
                <li class="page-item">
                  <a class="page-link"
                    href="${createURL(nbPages - 1)}"
                    data-value="${nbPages - 1}"
                  >
                    Last
                  </a>
                </li>
                `
            : ''
        }
      </ul>
    `;

    [...container.querySelectorAll('a')].forEach(element => {
        element.addEventListener('click', event => {
            event.preventDefault();
            refine(event.currentTarget.dataset.value);
        });
    });
};

// Create the custom widget
const customPagination = instantsearch.connectors.connectPagination(
    renderPagination
);

// Instantiate the custom widget
search.addWidgets([
    customPagination({
        container: document.querySelector('#pagination'),
    })
]);

search.start();