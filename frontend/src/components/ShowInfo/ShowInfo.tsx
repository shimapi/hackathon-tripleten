import ShowInfoTable from "../ShowInfo/ShowInfoTable";

const ShowInfo = () => {
	return (
		<div className="main">
			<h4>JSON Data Table</h4>
			<ShowInfoTable filename="ltv.json" />
			<ShowInfoTable filename="mean_invoice_by_region.json" />
			<ShowInfoTable filename="mean_sales_by_region.json" />
			<ShowInfoTable filename="sales_by_month.json" />
			<ShowInfoTable filename="sales_by_region.json" />
			<ShowInfoTable filename="sales_per_month.json" />
			<ShowInfoTable filename="top10_months_nsales.json" />
			<ShowInfoTable filename="top10_months_total.json" />
			<ShowInfoTable filename="top10_products_quantity.json" />
			<ShowInfoTable filename="top10_products_total.json" />
		</div>
	);
};

export default ShowInfo;
