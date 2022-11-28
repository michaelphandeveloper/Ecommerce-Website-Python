import React from 'react'
import { Row, Col } from 'react-bootstrap'
import products from '../products'
function HomeScreen() {
	return (
		<div>
			<h1>Sản Phẩm Mới Nhất</h1>
			<Row>
				{products.map(products => (
					<Col sm={12} md={6} lg={4} xl={3}>
						<h3>{products.name}</h3>
					</Col>
				))}
			</Row>
		</div>
	)
}

export default HomeScreen
