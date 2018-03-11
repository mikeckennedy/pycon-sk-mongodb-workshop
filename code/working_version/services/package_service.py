from data.downloads import Download
from data.packages import Package
from data.release_history import ReleaseHistory
from data.users import User


class PackageService:
    @classmethod
    def package_count(cls):
        return Package.objects().count()

    @classmethod
    def release_count(cls):
        return ReleaseHistory.objects().count()

    @classmethod
    def user_count(cls):
        return User.objects().count()

    @classmethod
    def download_count(cls):
        return Download.objects().count()

    @classmethod
    def popular_packages(cls, limit: int):
        return []

    @classmethod
    def maintainers(cls, package):
        return []

    @classmethod
    def find_package_by_name(cls, name):
        return Package.objects(name=name).first()

    @classmethod
    def latest_package_release(cls, package):
        return ReleaseHistory \
            .objects(package_id=package.id) \
            .order_by('-created') \
            .first()
