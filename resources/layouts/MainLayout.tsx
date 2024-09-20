import { Helmet, HelmetProvider } from 'react-helmet-async';

import favicon from '@/assets/favicon.ico';
import appleTouchIcon from '@/assets/apple-touch-icon.png';
import { Link } from '@tanstack/react-router';

interface MainLayoutProps {
  children: React.ReactNode;
  title: string;
  description: string;
  keywords: string;
}

const helmetContext = {};

const MainLayout = ({
  children,
  title,
  description,
  keywords,
}: MainLayoutProps) => {
  return (
    <HelmetProvider context={helmetContext}>
      <Helmet>
        <title>Z - Dashboard - {title}</title>
        <meta name="description" content={description} />
        <meta name="keywords" content={keywords} />
        <meta charSet="utf-8" />
        <link rel="icon" type="image/x-icon" href={favicon} />
        <link rel="icon" href={favicon} sizes="any" />
        <link rel="apple-touch-icon" href={appleTouchIcon} />
      </Helmet>
      <div className="p-2 flex gap-2">
        <Link to="/" className="[&.active]:font-bold">
          Home
        </Link>
        <Link to="/about" className="[&.active]:font-bold">
          About
        </Link>
      </div>
      <hr />
      <main>{children}</main>
    </HelmetProvider>
  );
};

export default MainLayout;
