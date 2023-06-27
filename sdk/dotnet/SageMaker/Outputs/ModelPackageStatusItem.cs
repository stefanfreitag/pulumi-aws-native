// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    /// <summary>
    /// Represents the overall status of a model package.
    /// </summary>
    [OutputType]
    public sealed class ModelPackageStatusItem
    {
        /// <summary>
        /// If the overall status is Failed, the reason for the failure.
        /// </summary>
        public readonly string? FailureReason;
        /// <summary>
        /// The name of the model package for which the overall status is being reported.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The current status.
        /// </summary>
        public readonly Pulumi.AwsNative.SageMaker.ModelPackageStatusItemStatus Status;

        [OutputConstructor]
        private ModelPackageStatusItem(
            string? failureReason,

            string name,

            Pulumi.AwsNative.SageMaker.ModelPackageStatusItemStatus status)
        {
            FailureReason = failureReason;
            Name = name;
            Status = status;
        }
    }
}
