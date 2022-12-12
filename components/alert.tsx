import Container from './container'

const Alert = () => {
  return (
    <div className="border-b bg-neutral-50 border-neutral-200">
      <Container>
        <div className="py-2 text-center text-sm">
            Learn more about me on {' '}
            <a
              href={`https:/jathurchan.com`}
              className="underline hover:text-blue-600 duration-200 transition-colors"
            >
              jathurchan.com
            </a>
            .
        </div>
      </Container>
    </div>
  )
}

export default Alert
