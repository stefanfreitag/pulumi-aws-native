// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NimbleStudio.Outputs
{

    [OutputType]
    public sealed class StudioComponentStudioComponentConfiguration
    {
        public readonly Outputs.StudioComponentActiveDirectoryConfiguration? ActiveDirectoryConfiguration;
        public readonly Outputs.StudioComponentComputeFarmConfiguration? ComputeFarmConfiguration;
        public readonly Outputs.StudioComponentLicenseServiceConfiguration? LicenseServiceConfiguration;
        public readonly Outputs.StudioComponentSharedFileSystemConfiguration? SharedFileSystemConfiguration;

        [OutputConstructor]
        private StudioComponentStudioComponentConfiguration(
            Outputs.StudioComponentActiveDirectoryConfiguration? activeDirectoryConfiguration,

            Outputs.StudioComponentComputeFarmConfiguration? computeFarmConfiguration,

            Outputs.StudioComponentLicenseServiceConfiguration? licenseServiceConfiguration,

            Outputs.StudioComponentSharedFileSystemConfiguration? sharedFileSystemConfiguration)
        {
            ActiveDirectoryConfiguration = activeDirectoryConfiguration;
            ComputeFarmConfiguration = computeFarmConfiguration;
            LicenseServiceConfiguration = licenseServiceConfiguration;
            SharedFileSystemConfiguration = sharedFileSystemConfiguration;
        }
    }
}
