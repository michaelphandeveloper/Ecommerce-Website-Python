import React from 'react'
import { Navbar, Nav, Container, Row } from 'react-bootstrap'

function Header() {
	return (
		<header>
			<Navbar bg="light" expand="lg">
        <Container>
				<Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
				<Navbar.Toggle aria-controls="basic-navbar-nav" />
				<Navbar.Collapse id="basic-navbar-nav">
					<Nav className="me-auto">
						<Nav.Link href="#home">Home</Nav.Link>
						<Nav.Link href="#link">Link</Nav.Link>
					</Nav>
          </Container>
				</Navbar.Collapse>
			</Navbar>
		</header>
	)
}

export default Header
