const InputPlaceholder = {
    inputs: document.querySelectorAll("input[name]"),
    in(e) {
        const ann = e.currentTarget.previousElementSibling;
        if (ann.tagName == 'P')
            ann.classList.add("annotation_active");
    },
    out(e) {
        const ann = e.currentTarget.previousElementSibling;
        if (e.target.value == "")
            ann.classList.remove("annotation_active");
    },
    reload(input) {
        const ann = input.previousElementSibling;

        if (ann.tagName == 'P')
            ann.classList.add("annotation_active");
    }
}

for (const input of InputPlaceholder.inputs) {
    input.addEventListener("focus", InputPlaceholder.in);
    input.addEventListener("focusout", InputPlaceholder.out);

    // console.log(input)
    setTimeout(() => {
        if (input.value != '')
            InputPlaceholder.reload(input)
    }, 3000);
}
