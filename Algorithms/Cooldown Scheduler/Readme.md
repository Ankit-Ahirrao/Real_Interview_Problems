# 3. Cooldown Scheduler

Given a string with characters representing separate tasks and integer cooldown `k`, return a string padded with an empty task '.' so that any duplicate tasks are separated by at least `k` tasks between them.

The order of the tasks should be preserved; do not re-order the given tasks to reduce the size of the output.
Example function calls and return values:

    schedule('aba', 2) => 'ab.a'
    // the last "a" needs a padded task inserted as specified by the cooldown 
    integerschedule('abca', 2) => 'abca'
    // no need to insert padded tasks, as there are no duplicate tasks within the cooldown windowschedule('aabb', 2) => 'a..ab..b' 
    // each duplicate task requires empty tasks to be inserted as specified by the cooldown int. The first b cannot be queued until after the last a.schedule('acbab', 3) => 'acb.a.b'