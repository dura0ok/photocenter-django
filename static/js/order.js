import Toastify from 'toastify-js'
import "toastify-js/src/toastify.css"

 function onAlpineReady() {
        Alpine.data("app", function () {
          return {
            submitButtonLabel: "Отправить",
            components: {
              services: [],
              film: [],
              print: [],
            },
            onSubmit() {
              const result = {};

              Object.keys(this.components).map((key) => {
                const mappedDivs = this.components[key].map((div) => {
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

              const currentUrl = window.location.href

              console.log(result);
              console.log(JSON.stringify(result))
              fetch(currentUrl, {
                method: "POST",
                body: JSON.stringify(result),
                contentType: 'application/json; charset=utf-8',
              }).then((response) => {
                response.json().then(r => console.log(r))
              })
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
                count: 0,
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
          };
        });
      }

      document.addEventListener("alpine:init", onAlpineReady);