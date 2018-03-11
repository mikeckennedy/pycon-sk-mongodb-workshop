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
        packages = Package.objects()\
            .order_by('-total_downloads')\
            .limit(limit)\
            .all()

        return list(packages)

    @classmethod
    def maintainers(cls, package):
        return User.objects(id__in=package.maintainers)

    @classmethod
    def covered_releases(cls, ratio_covered:float):
        return ReleaseHistory\
            .objects(health__coverage__gte=ratio_covered)

    @classmethod
    def find_package_by_name(cls, name):
        return Package.objects(name=name).first()

    @classmethod
    def latest_package_release(cls, package):
        return ReleaseHistory \
            .objects(package_id=package.id) \
            .order_by('-created') \
            .first()
