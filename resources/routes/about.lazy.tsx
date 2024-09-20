import MainLayout from '@/layouts/MainLayout';
import { createLazyFileRoute } from '@tanstack/react-router';

export const Route = createLazyFileRoute('/about')({
  component: About,
});

function About() {
  return (
    <MainLayout
      title="About"
      description="About page"
      keywords="about, z butler"
    >
      <div className="p-2">Hello from About!</div>

      <p>idk if this will work or not lol</p>
    </MainLayout>
  );
}
