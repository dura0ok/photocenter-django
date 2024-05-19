import Toastify from 'toastify-js'
import {showErrorToast} from "./toasts";
function onAlpineReady() {
        Alpine.data("app", function () {
          return {
            status: '',
            submitButtonLabel: "Кастомный текст кнопки",
            components: {
              services: [],
              items: [],
              print: [],
            },
            clients: "",
            urgency: false,
            getJson() {
              const result = {};

              Object.keys(this.components).map((key) => {
                const mappedDivs = this.components[key]
                  .filter((div) => div.count >= 1 && div.option !== "")
                  .map((div) => {
                    const newDiv = { ...div };
                    if (div.dropdownValues.length === 0) {
                      delete newDiv.dropdownValues;
                    }

                    if (Object.keys(div.customFields).length === 0) {
                      delete newDiv.customFields;
                    }

                    return newDiv;
                  });

                result[key] = mappedDivs;
              });

              result.client_id = this.clients;
              result.urgency = this.urgency


              this.status = JSON.stringify(result);
              console.log(result)
              //console.log(this.status);

              return result;
            },
            onChange() {
              /**
               * Кастомная логика
               */
              console.log("Кастомная логика!!!");

              const json = this.getJson();

              console.log(`Json из onChange!!!!!!:`, json);

              const currentUrl = window.location.href

              fetch(`${currentUrl}/calculate`, {
                method: "POST",
                body: JSON.stringify(json),
                contentType: 'application/json; charset=utf-8',
              }).then((response) => {
                response.json().then(r => {
                  if(r['error']){
                    this.status = ''
                    showErrorToast(r['error'])
                    return
                  }

                  const totalCost =
                    parseFloat(r['services_cost']) +
                    parseFloat(r['items_cost']) +
                    parseFloat(r['print_cost']);

                  // Создание текстовой части с разбивкой стоимостей и общей стоимостью
                  this.status = `
                    Стоимость услуг: $${parseFloat(r['services_cost']).toFixed(2)}
                    Стоимость товаров: $${parseFloat(r['items_cost']).toFixed(2)}
                    Стоимость печати: $${parseFloat(r['print_cost']).toFixed(2)}
                    Общая стоимость до скидок и срочности: $${totalCost.toFixed(2)}
                    Итоговая стоимость $${parseFloat(r['general_cost']).toFixed(2)}
                  `
                })
              })
            },
            onSubmit() {
              const data = this.getJson();
              console.log(data)
              console.log("onSubmit");

              /**
               * Логика отправки формы
               */
            },
          };
        });

        Alpine.data("optionsSelector", function () {
          return {
            onAddDiv() {
              const customFields = {};

              if (this.customFields && this.customFields.length > 0) {
                this.customFields.map(
                  (field) => (customFields[field.name] = "")
                );
              }

              this.divs.push({
                option: "",
                count: 1,
                dropdownValues: [],
                customFields: customFields,
              });
            },
            onDeleteDiv(index) {
              this.divs.splice(index, 1);
            },
            onOptionChanged(div) {
              const option = this.availableOptions.find(
                (option) => option.id === this.$event.target.value
              );

              div.option = option;
            },
            onCountChanged(div) {
              console.log(this.$event.target.value !== "");
              if (this.$event.target.value !== "" && div.count < 1) {
                div.count = 1;
              }

               if (this.maxOptionsCount && this.maxOptionsCount[parseInt(div.option)]) {
                const maxValue = this.maxOptionsCount[parseInt(div.option)];

                if (maxValue < this.$event.target.value) {
                  div.count = this.maxOptionsCount[parseInt(div.option)];

                  Toastify({
                    text: "Превышено максимальное значение для данного элемента",
                  }).showToast();
                }
              }

              this.onChange();
            },

          };
        });
      }

      document.addEventListener("alpine:init", onAlpineReady);