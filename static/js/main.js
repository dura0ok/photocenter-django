import {TabulatorFull as Tabulator} from 'tabulator-tables';

document.querySelectorAll(".query-execute").forEach((btn) => {
    btn.addEventListener("click", (e) => {
        const queryWrapper = e.target.parentNode;
        const resultsWrapper = queryWrapper.querySelector(".results")
        resultsWrapper.innerHTML = ""

        const queryResultCount = Math.floor(Math.random() * 5) + 1;

        for (let i = 0; i < queryResultCount; i++) {
            const queryResultDiv = document.createElement('div');
            queryResultDiv.classList.add('query-result');
            resultsWrapper.appendChild(queryResultDiv);

            const columns = generateRandomColumns();
            const data = generateRandomData();

            new Tabulator(queryResultDiv, {
                columns: columns,
                data: data,
                layout: "fitDataTable"
            });
        }


    });
});

function generateRandomColumns() {
    const columnCount = Math.floor(Math.random() * 5) + 1;
    const columns = [];
    for (let i = 0; i < columnCount; i++) {
        columns.push({title: 'Column ' + (i + 1), field: 'field' + (i + 1)});
    }
    return columns;
}

function generateRandomData() {
    const rowCount = Math.floor(Math.random() * 10) + 1;
    const data = [];
    for (let i = 0; i < rowCount; i++) {
        const row = {};
        for (let j = 0; j < 5; j++) {
            row['field' + (j + 1)] = 'Data ' + (i + 1) + '-' + (j + 1);
        }
        data.push(row);
    }
    return data;
}


function updateIcon(cell, formatterParams, onRendered) {
    return "<i class='fa fa-edit'></i>";
}

function deleteIcon(cell, formatterParams, onRendered) {
    return "<i class='fa fa-trash'></i>";
}

function initializeTable(selector) {
    const tableColumns = generateRandomColumns();
    const tableData = generateRandomData();

    new Tabulator(selector, {
        data: tableData,
        columns: tableColumns.concat([
            {
                title: "Update", formatter: updateIcon, width: 100, hozAlign: "center", cellClick: function (e, cell) {
                    alert("Update action for: " + JSON.stringify(cell.getRow().getData()));
                }
            },
            {
                title: "Delete", formatter: deleteIcon, width: 100, hozAlign: "center", cellClick: function (e, cell) {
                    alert("Delete action for: " + JSON.stringify(cell.getRow().getData()));
                }
            }
        ]),
        layout: "fitColumns",
        pagination: "local", // Enable pagination
        paginationSize: 2, // Number of rows per page
    });
}

initializeTable(document.querySelector(".edit-clients-table"))