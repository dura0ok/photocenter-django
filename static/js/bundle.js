/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "../static/js/main.js":
/*!****************************!*\
  !*** ../static/js/main.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _scss_main_scss__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../scss/main.scss */ "../static/scss/main.scss");
/* harmony import */ var _scss_main_scss__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_scss_main_scss__WEBPACK_IMPORTED_MODULE_0__);
Object(function webpackMissingModule() { var e = new Error("Cannot find module 'tabulator-tables'"); e.code = 'MODULE_NOT_FOUND'; throw e; }());


document.querySelectorAll(".query-execute").forEach(function (btn) {
  btn.addEventListener("click", function (e) {
    var queryWrapper = e.target.parentNode;
    var resultsWrapper = queryWrapper.querySelector(".results");
    resultsWrapper.innerHTML = "";
    var queryResultCount = Math.floor(Math.random() * 5) + 1;
    for (var i = 0; i < queryResultCount; i++) {
      var queryResultDiv = document.createElement('div');
      queryResultDiv.classList.add('query-result');
      resultsWrapper.appendChild(queryResultDiv);
      var columns = generateRandomColumns();
      var data = generateRandomData();
      new Object(function webpackMissingModule() { var e = new Error("Cannot find module 'tabulator-tables'"); e.code = 'MODULE_NOT_FOUND'; throw e; }())(queryResultDiv, {
        columns: columns,
        data: data,
        layout: "fitDataTable"
      });
    }
  });
});
function generateRandomColumns() {
  var columnCount = Math.floor(Math.random() * 5) + 1;
  var columns = [];
  for (var i = 0; i < columnCount; i++) {
    columns.push({
      title: 'Column ' + (i + 1),
      field: 'field' + (i + 1)
    });
  }
  return columns;
}
function generateRandomData() {
  var rowCount = Math.floor(Math.random() * 10) + 1;
  var data = [];
  for (var i = 0; i < rowCount; i++) {
    var row = {};
    for (var j = 0; j < 5; j++) {
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
  var tableColumns = generateRandomColumns();
  var tableData = generateRandomData();
  new Object(function webpackMissingModule() { var e = new Error("Cannot find module 'tabulator-tables'"); e.code = 'MODULE_NOT_FOUND'; throw e; }())(selector, {
    data: tableData,
    columns: tableColumns.concat([{
      title: "Update",
      formatter: updateIcon,
      width: 100,
      hozAlign: "center",
      cellClick: function cellClick(e, cell) {
        alert("Update action for: " + JSON.stringify(cell.getRow().getData()));
      }
    }, {
      title: "Delete",
      formatter: deleteIcon,
      width: 100,
      hozAlign: "center",
      cellClick: function cellClick(e, cell) {
        alert("Delete action for: " + JSON.stringify(cell.getRow().getData()));
      }
    }]),
    layout: "fitColumns",
    pagination: "local",
    // Enable pagination
    paginationSize: 2 // Number of rows per page
  });
}
initializeTable(document.querySelector(".edit-clients-table"));

/***/ }),

/***/ "../static/scss/main.scss":
/*!********************************!*\
  !*** ../static/scss/main.scss ***!
  \********************************/
/***/ (() => {

throw new Error("Module build failed (from ./node_modules/mini-css-extract-plugin/dist/loader.js):\nModuleBuildError: Module build failed (from ./node_modules/css-loader/dist/cjs.js):\nError: Can't resolve '../node_modules/tabulator-tables/dist/css/tabulator.min.css' in '/home/durachok/workspace/photo_center/static/scss'\n    at finishWithoutResolve (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/Resolver.js:564:18)\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/Resolver.js:656:15\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/Resolver.js:714:5\n    at eval (eval at create (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:16:1)\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/Resolver.js:714:5\n    at eval (eval at create (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:16:1)\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/Resolver.js:714:5\n    at eval (eval at create (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:15:1)\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/Resolver.js:714:5\n    at eval (eval at create (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:16:1)\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/Resolver.js:714:5\n    at eval (eval at create (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:16:1)\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/Resolver.js:714:5\n    at eval (eval at create (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:16:1)\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/Resolver.js:714:5\n    at eval (eval at create (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:16:1)\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/Resolver.js:714:5\n    at eval (eval at create (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:15:1)\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/enhanced-resolve/lib/DirectoryExistsPlugin.js:41:15\n    at process.processTicksAndRejections (node:internal/process/task_queues:81:21)\n    at processResult (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/webpack/lib/NormalModule.js:841:19)\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/webpack/lib/NormalModule.js:966:5\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/loader-runner/lib/LoaderRunner.js:400:11\n    at /home/durachok/workspace/photo_center/frontent-bundler/node_modules/loader-runner/lib/LoaderRunner.js:252:18\n    at context.callback (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/loader-runner/lib/LoaderRunner.js:124:13)\n    at Object.loader (/home/durachok/workspace/photo_center/frontent-bundler/node_modules/css-loader/dist/index.js:155:5)\n    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	__webpack_require__("../static/js/main.js");
/******/ 	// This entry module is referenced by other modules so it can't be inlined
/******/ 	var __webpack_exports__ = __webpack_require__("../static/scss/main.scss");
/******/ 	
/******/ })()
;