// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Outputs
{

    [OutputType]
    public sealed class DataSourceOneDriveUsers
    {
        public readonly ImmutableArray<string> OneDriveUserList;
        public readonly Outputs.DataSourceS3Path? OneDriveUserS3Path;

        [OutputConstructor]
        private DataSourceOneDriveUsers(
            ImmutableArray<string> oneDriveUserList,

            Outputs.DataSourceS3Path? oneDriveUserS3Path)
        {
            OneDriveUserList = oneDriveUserList;
            OneDriveUserS3Path = oneDriveUserS3Path;
        }
    }
}
