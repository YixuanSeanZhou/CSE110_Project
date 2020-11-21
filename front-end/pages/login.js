import { Form, Button, Navbar } from 'react-bootstrap'
import Image from 'next/image'
import Link from 'next/link'
import Particles from 'react-particles-js';

import styles from '../styles/Register.module.css'

import { GaryNavbar } from '../components/commonUI'

export default function Login() {
	return (
		<>
			<GaryNavbar>
				<Navbar.Text>Log in</Navbar.Text>
			</GaryNavbar>
			<div className={styles.outer}>
				<Particles
						params={{
							"particles": {
							"number": {
							"value": 90,
							"density": {
							"enable": true,
							"value_area": 2000
							}
							},
							"color": {
							"value": "#ffffff"
							},
							"size": {
							"value": 2.5
							}
						},
							"interactivity": {
							"events": {
							"onhover": {
							"enable": true,
							"mode": "repulse"
							}
							}
							}
						}}/>
				<div className={styles.middle} style={{
                    position: "absolute",
                    top: "20%",
                    left: 0,
                    width: "100%",
                    height: "absolute"
					
                }}>
					<div className={styles.login}>
						<Form.Group style={{ display: 'flex', alignItems: 'center' }}>
							<a href="/intro">
								<Image
									id="loginlogo"
									src="/logo/PCLogo-Color.svg"
									height="70"
									width="49"
									alt="logo"
									className=""
								/>
							</a>
							<h3 className="mt-3 ml-1" style={{ paddingLeft: '10px' }}>
								Gary <br /> Planner
							</h3>
						</Form.Group>

						<h3>Log in</h3>
						<Form>
							<Form.Group>
								<Form.Label htmlFor="username">Username</Form.Label>

								<Form.Control type="text" id="username" name="username" />
							</Form.Group>

							<Form.Group>
								<Form.Label htmlFor="passowrd">Passowrd</Form.Label>
								<Form.Control
									type="password"
									id="password"
									name="password"
								/>
							</Form.Group>

							<Form.Group>
								<Form.Label>
									<Form.Check
										type="checkbox"
										name="remember"
										label="Remember me"
									/>
								</Form.Label>
							</Form.Group>

							<Form.Group className="mt-1">
								<Form.Text style={{ fontSize: '.85rem' }}>
									New to GaryPlanner?{' '}
									<a href="/signup" style={{ color: '#0067b8' }}>
										Create an account
									</a>
								</Form.Text>
							</Form.Group>
							<div style={{ textAlign: 'right' }}>
								<Button
									type="submit"
									value="submit"
									className="bg-orange mt-3">
									Login
								</Button>{' '}
							</div>
						</Form>
					</div>
				</div>
			</div>
		</>
	)
}
