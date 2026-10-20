document.addEventListener('DOMContentLoaded', function() {
    // Find the file input field (Django usually names it by field name)
    const fileInput = document.getElementById('id_xml_file');
    
    if (fileInput) {
        fileInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            
            reader.onload = function(e) {
                const xmlText = e.target.result;
                
                // Parse the XML string into a DOM object
                const parser = new DOMParser();
                const xmlDoc = parser.parseFromString(xmlText, "text/xml");
                
                const getTagValue = (tagName) => {
                    const element = xmlDoc.querySelector(tagName);
                    return element ? element.textContent.trim() : '';
                };

                // Extract values from XML tags
                const KeyValue = xmlDoc.getElementsByTagName("chNFe")[0]?.textContent || '';
                const nNF = getTagValue('nNF');
                const dhEmi = getTagValue('dhEmi');
                const serie_notaS = xmlDoc.getElementsByTagName("serie")[0]?.textContent || '';

                const emitCNPJ = xmlDoc.querySelector('emit CNPJ')?.textContent.trim() || '';
                const emitNome = xmlDoc.querySelector('emit xNome')?.textContent.trim() || '';
                const destCNPJ = xmlDoc.querySelector('dest CNPJ')?.textContent.trim() || '';
                const destNome = xmlDoc.querySelector('dest xNome')?.textContent.trim() || '';
                const vNF = getTagValue('vNF');


                const cProd = getTagValue('cProd');       // Product Code ("1004")
                const xProd = getTagValue('xProd');       // Product Name ("ETANOL HIDRATADO...")
                const qCom = getTagValue('qCom');         // Quantity ("27.8310")
                const vProd = xmlDoc.querySelector('prod vProd')?.textContent.trim() || ''; // Item Price
                console.log('Product Details:', { cProd, xProd, qCom, vProd });
                const productDetails = {
                    cProd: cProd,
                    xProd: xProd,
                    qCom: qCom,
                    vProd: vProd
                };
                // console.log(dhEmi) 
                // Map values to Django admin input fields
                const key = document.getElementById('id_key');
                const value = document.getElementById('id_value');
                const cnpj_fornecedor = document.getElementById('id_cnpj_fornecedor');
                const cnpj_cliente = document.getElementById('id_cnpj_cliente');
                const numero_nota = document.getElementById('id_title');
                const serie_NF = document.getElementById('id_serie_nota');
                 
                if (productDetails.cProd && productDetails.xProd && productDetails.qCom && productDetails.vProd) {
                    const productDetailsField = document.getElementById('id_produtos_nota');
                    if (productDetailsField) {
                        productDetailsField.value = JSON.stringify(productDetails);
                    }
                }
                if (key) key.value = KeyValue;
                if (value) value.value = vNF;
                if (cnpj_fornecedor) cnpj_fornecedor.value = emitCNPJ;
                if (cnpj_cliente) cnpj_cliente.value = destCNPJ;
                if (numero_nota) numero_nota.value = nNF;
                if (serie_NF) serie_NF.value = serie_notaS;
            };

            reader.readAsText(file);
        });
    }
});