const ips = [
    {
      address: "192.168.0.2",
      mask: "255.255.255.0"
    },
    {
      address: "192.168.0.10",
      mask: "255.255.255.0"
    },
    {
      address: "192.168.0.26",
      mask: "255.255.255.0"
    },
    {
      address: "192.168.0.30",
      mask: "255.255.255.0"
    }
  ]
  
  const table = document.querySelector('.table_ips')
  for (let i of ips){
        let tr1 = `<tr>
        <td>${i.address}</td>
        <td>${i.mask}</td>
        </tr>`
        table.insertAdjacentHTML('beforeend', tr1)
  }

