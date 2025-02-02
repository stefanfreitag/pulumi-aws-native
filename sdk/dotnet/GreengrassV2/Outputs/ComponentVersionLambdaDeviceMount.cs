// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GreengrassV2.Outputs
{

    [OutputType]
    public sealed class ComponentVersionLambdaDeviceMount
    {
        public readonly bool? AddGroupOwner;
        public readonly string? Path;
        public readonly Pulumi.AwsNative.GreengrassV2.ComponentVersionLambdaFilesystemPermission? Permission;

        [OutputConstructor]
        private ComponentVersionLambdaDeviceMount(
            bool? addGroupOwner,

            string? path,

            Pulumi.AwsNative.GreengrassV2.ComponentVersionLambdaFilesystemPermission? permission)
        {
            AddGroupOwner = addGroupOwner;
            Path = path;
            Permission = permission;
        }
    }
}
