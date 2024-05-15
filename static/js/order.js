const orderForm = document.querySelector('.order-creation-wrapper form')
const servicesOrderWrapper = document.querySelector(".services-info")
const servicesWrapper = servicesOrderWrapper.querySelector('.services')
const serviceCreateBtn = servicesOrderWrapper.querySelector(".service-create-btn")
const btnTag = "button"
const containerWithSelectorClass = "options-selector"
const codesContainerClass = "codes-container"

const createServiceSelectAndInput = (data, key, selectCallback, inputCallback) => {
    const container = document.createElement("div");
    container.classList.add(`.${containerWithSelectorClass}`);

    const select = document.createElement('select');
    data.forEach(item => {
        console.log(item)
        const option = document.createElement('option');
        option.value = item[key];
        option.text = item[key];
        select.appendChild(option);
    });

    select.addEventListener('change', (e) => selectCallback(e.target));

    const countInput = document.createElement('input');
    countInput.setAttribute('min', '0');
    countInput.addEventListener('change', (e) => inputCallback(e.target))
    countInput.type = 'number';
    countInput.placeholder = 'Количество';
    countInput.value = "0"

    container.appendChild(select)
    container.appendChild(countInput)
    return container
};


const onServiceSelectChange = (select) => {
    const serviceWrapper = select.closest('div')
    onServiceInputChange(serviceWrapper.querySelector('input'))
}

const onServiceInputChange = (inputTarget) => {
    const quantity = inputTarget.value
    const serviceWrapper = inputTarget.closest('div')
    const select = serviceWrapper.querySelector('select');
    const selectedEl = select.options[select.selectedIndex]
    let codesContainer = serviceWrapper.querySelector(`${codesContainerClass}`)

    if(selectedEl.value !== "Проявка плёнки"){
        if(codesContainer){
            codesContainer.remove()
        }
        return
    }
    debugger;
    if(!codesContainer){
        const newCodesContainer = document.createElement('div')
        newCodesContainer.classList.add(`${codesContainerClass}`)
        serviceWrapper.appendChild(newCodesContainer)
        codesContainer = newCodesContainer
    }
    console.log(codesContainer, codesContainer.querySelectorAll('input'))
    codesContainer.querySelectorAll('input').forEach(el => el.remove())

    for(let i = 0; i < quantity; i++) {
        const el = document.createElement("input");
        codesContainer.appendChild(el)
    }
}



const servicesData = [
            { name: "Ретушь", price: 50 },
            { name: "Фото на Паспорт", price: 100 },
            { name: "Проявка плёнки", price: 10 }
];


serviceCreateBtn.addEventListener("click", (e) => {
    e.preventDefault();
    const serviceInputsContainer = createServiceSelectAndInput(
        servicesData,
        "name",
        onServiceSelectChange,
        onServiceInputChange
    );
    servicesWrapper.appendChild(serviceInputsContainer)
})

serviceCreateBtn.click()