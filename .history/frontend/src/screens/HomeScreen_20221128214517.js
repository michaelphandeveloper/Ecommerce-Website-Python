import React from 'react'
import { Row, Col } from 'react-bootstrap'
import products from '.../products'
function HomeScreen() {
	return (
		<div>
			<h1>Sản Phẩm Mới Nhất</h1>
			<Row>
				{products.map(products => (
					<Col></Col>
				))}
			</Row>
		</div>
	)
}

export default HomeScreen
