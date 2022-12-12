import Alert from './alert'
import Footer from './footer'
import Meta from './meta'

type Props = {
  children: React.ReactNode
}

const Layout = ({ children }: Props) => {
  return (
    <>
      <Meta />
      <div className="min-h-screen">
        <Alert />
        <main>{children}</main>
      </div>
      <Footer />
    </>
  )
}

export default Layout
