// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WorkSpaces.Outputs
{

    [OutputType]
    public sealed class WorkspaceWorkspaceProperties
    {
        public readonly string? ComputeTypeName;
        public readonly int? RootVolumeSizeGib;
        public readonly string? RunningMode;
        public readonly int? RunningModeAutoStopTimeoutInMinutes;
        public readonly int? UserVolumeSizeGib;

        [OutputConstructor]
        private WorkspaceWorkspaceProperties(
            string? computeTypeName,

            int? rootVolumeSizeGib,

            string? runningMode,

            int? runningModeAutoStopTimeoutInMinutes,

            int? userVolumeSizeGib)
        {
            ComputeTypeName = computeTypeName;
            RootVolumeSizeGib = rootVolumeSizeGib;
            RunningMode = runningMode;
            RunningModeAutoStopTimeoutInMinutes = runningModeAutoStopTimeoutInMinutes;
            UserVolumeSizeGib = userVolumeSizeGib;
        }
    }
}
