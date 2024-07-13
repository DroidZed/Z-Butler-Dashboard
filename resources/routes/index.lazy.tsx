import MainLayout from '@/layouts/MainLayout';
import { createLazyFileRoute } from '@tanstack/react-router';

export const Route = createLazyFileRoute('/')({
  component: Index,
});

function Index() {
  return (
    <MainLayout title="Home" description="Home page" keywords="home, z butler">
      <div className="p-2">
        <h3>Welcome Home!</h3>
      </div>
    </MainLayout>
  );
}
