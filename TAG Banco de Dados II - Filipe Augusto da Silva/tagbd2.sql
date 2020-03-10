/*5) Qual é o vendedor que possui a melhor avaliação média e maior quantidade de vendas?*/
	/*Maior quantidade de vendas*/
select count(compra.idCompra) as `qtde_vendas`, produto.vendedor, vendedor.nome
from compra inner join produto on compra.produto = produto.idproduto
inner join vendedor on produto.vendedor = vendedor.idvendedor
group by produto.vendedor order by `qtde_vendas` DESC limit 1;

	/*Melhor avaliação média*/
select `avaliacao vendedor`.vendedor, vendedor.nome, AVG(cast(`avaliacao vendedor`.nota as decimal(5,2))) as `media`
from `avaliacao vendedor` inner join vendedor on `avaliacao vendedor`.vendedor = vendedor.idvendedor
group by vendedor order by `media` DESC limit 1;

/*RESPOSTA:
	Maior quantidade de vendas:
		vendedor: 798
        nome: welbert
        qtde_vendas: 101

	Melhor avaliação:
		vendedor: 179
		nome: hanna
        media: 6.86
*/

/*4) Qual produto que tem a melhor avaliação e o menor preço?*/
	/*Melhor avaliação*/
SELECT `avaliacao produto`.*, produto.* FROM `avaliacao produto` inner join produto on produto.idproduto = `avaliacao produto`.produto where `avaliacao produto`.nota like '10' order by produto.preco limit 1;

	/*Menor preço*/
select * from produto order by preco;
    
/*RESPOSTA: 
	Melhor avaliação (mostrando apenas UM resultado):
		produto: 12714
        item: CAMISA 67746 1923
        nota: 10
        preco: 10.07
	
    Menor preço:
		produto: 3451
        item: CAMISA Thorsby 1970
        preço: 10.04
*/

/*3) Qual é o nome do comprador mais jovem?*/
select nome from fregueses order by data_nasc DESC limit 1;
/*RESPOSTA: geny */

/*2) Qual é o nome do primeiro comprador, em ordem alfabética, que tenha nascido após 1990?*/
select nome from fregueses where YEAR (fregueses.data_nasc) > 1990 order by nome limit 1;
/*RESPOSTA: adela */

/*1) Qual foi o total de compras feitas nesse mercado?*/
select count(produto.preco) as 'Número de compras', sum(produto.preco) as 'Somatório dos valores' from compra inner join produto on compra.produto=produto.idproduto;
/*RESPOSTA:
	Número de compras: 50000
    Somatório dos valores: 12822636.84 */