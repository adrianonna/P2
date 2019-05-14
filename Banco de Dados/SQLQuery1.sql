select idproduto, nome as produto, quantest as [estoque real], estmin as [estoque minimo], 'Num.Ref' as Referencia
from Produto

select venda, custo, (venda- custo) as diferenca
from produto

select venda, venda*1.25 as "aumento real", venda*0.25 as porcentagem
from Produto

--lista 2 ex 1
select * from setor

select se.nome, se.idsetor, fu.nome
from setor se join funcionario fu
on fu.idfuncionario = se.idchefe
order by 1

select * from produto

select pr.idproduto, ti.nome, pr.nome, pr.quantest, pr.venda, (pr.quantest * pr.venda) "valor total"
from produto pr join tipo ti
on ti.idtipo = pr.idtipo

select ti.nome, SUM(pr.quantest), SUM(pr.quantest * pr.venda)
from tipo ti join produto pr
on ti.idtipo = pr.idtipo
group by ti.nome
order by 1


select COUNT(cli.idcliente), ci.nome
from cliente cli join cidade ci
on ci.idcidade = cli.idcidade
group by ci.nome
order by COUNT(cli.idcliente), ci.nome


select func.nome, fu.sexo, count(fu.idfuncionario)
from funcionario fu join funcao func
on func.idfuncao = fu.idfuncao
where fu.email is NULL
group by fu.sexo, func.nome
order by fu.sexo, func.nome

--6
--nome produto
--nome do tipo
--preco medio de custo
--preco medio de venda
--e diferenca custo e venda (avg)
--order nome produto

select pr.nome, ti.nome, 
AVG(pr.custo) "custo medio", 
AVG(pr.venda) "venda media", 
AVG(pr.custo) - AVG(pr.venda) as diferenca
from produto pr join tipo ti
on ti.idtipo = pr.idtipo
group by pr.nome, ti.nome
order by pr.nome

--exibir nome sigla total de salarios 
--por sexo de cada setor
--order nome setor

select se.nome, se.idsetor, sum(fu.salario),  fu.sexo
from setor se join funcionario fu
on se.idsetor = fu.idsetor
group by se.nome, se.idsetor, fu.sexo
order by se.nome

--8
--exibir o nome de cada funcao
--a quantidade de homens e mulheres
--total salario p sexo
--para as func where total salario 
--sexo > 1000
--order by nome funcao

select funcao.nome, fu.sexo, sum(fu.idfuncionario) "total func", sum(fu.salario) "salario total"
from funcao funcao join funcionario fu
on funcao.idfuncao = fu.idfuncao
where fu.salario > 1000
group by funcao.nome, fu.sexo
order by funcao.nome

--9
--exibir a lista de pedidos com o nome do cliente e do vendedor e o valor total de cada pedido order codigo pedido
select ped.idpedido, cli.nome, vend.nome, sum(item.preco * item.quant) as "valor total"
from pedido ped join cliente cli
on cli.idcliente = ped.idcliente
join funcionario vend
on vend.idfuncionario = ped.idvendedor
join itens item
on ped.idpedido = item.idpedido
group by ped.idpedido, cli.nome, vend.nome
order by ped.idpedido









































