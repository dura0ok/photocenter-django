const orderForm = document.querySelector('.order-creation-wrapper form')
const servicesOrderWrapper = document.querySelector(".services-info")
const servicesWrapper = servicesOrderWrapper.querySelector('.services')
const serviceCreateBtn = servicesOrderWrapper.querySelector(".service-create-btn")
const btnTag = "button"
const containerWithSelectorClass = "option-selector"


const createServiceSelectAndInput = (data, key, selectCallback, inputCallback) => {
    const container = document.createElement("div");
    container.classList.add("option-selector");

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

    container.appendChild(select)
    container.appendChild(countInput)
    return container
};


const onServiceSelectChange = (select) => {
    const selectedIndex = select.selectedIndex
    const selectedOption = select.options[selectedIndex]
    console.log(selectedOption)
    console.log(selectedOption.value)
}

const onServiceInputChange = (inputTarget) => {
    console.log(inputTarget)
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