// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Outputs
{

    /// <summary>
    /// The minimum and maximum amount of memory per vCPU, in GiB.
    /// </summary>
    [OutputType]
    public sealed class LaunchTemplateMemoryGiBPerVCpu
    {
        /// <summary>
        /// The maximum amount of memory per vCPU, in GiB.
        /// </summary>
        public readonly double? Max;
        /// <summary>
        /// TThe minimum amount of memory per vCPU, in GiB.
        /// </summary>
        public readonly double? Min;

        [OutputConstructor]
        private LaunchTemplateMemoryGiBPerVCpu(
            double? max,

            double? min)
        {
            Max = max;
            Min = min;
        }
    }
}
