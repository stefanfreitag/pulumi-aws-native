// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Route53RecoveryReadiness
{
    public static class GetReadinessCheck
    {
        /// <summary>
        /// Aws Route53 Recovery Readiness Check Schema and API specification.
        /// </summary>
        public static Task<GetReadinessCheckResult> InvokeAsync(GetReadinessCheckArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetReadinessCheckResult>("aws-native:route53recoveryreadiness:getReadinessCheck", args ?? new GetReadinessCheckArgs(), options.WithDefaults());

        /// <summary>
        /// Aws Route53 Recovery Readiness Check Schema and API specification.
        /// </summary>
        public static Output<GetReadinessCheckResult> Invoke(GetReadinessCheckInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetReadinessCheckResult>("aws-native:route53recoveryreadiness:getReadinessCheck", args ?? new GetReadinessCheckInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetReadinessCheckArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the ReadinessCheck to create.
        /// </summary>
        [Input("readinessCheckName", required: true)]
        public string ReadinessCheckName { get; set; } = null!;

        public GetReadinessCheckArgs()
        {
        }
        public static new GetReadinessCheckArgs Empty => new GetReadinessCheckArgs();
    }

    public sealed class GetReadinessCheckInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the ReadinessCheck to create.
        /// </summary>
        [Input("readinessCheckName", required: true)]
        public Input<string> ReadinessCheckName { get; set; } = null!;

        public GetReadinessCheckInvokeArgs()
        {
        }
        public static new GetReadinessCheckInvokeArgs Empty => new GetReadinessCheckInvokeArgs();
    }


    [OutputType]
    public sealed class GetReadinessCheckResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the readiness check.
        /// </summary>
        public readonly string? ReadinessCheckArn;
        /// <summary>
        /// The name of the resource set to check.
        /// </summary>
        public readonly string? ResourceSetName;
        /// <summary>
        /// A collection of tags associated with a resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.ReadinessCheckTag> Tags;

        [OutputConstructor]
        private GetReadinessCheckResult(
            string? readinessCheckArn,

            string? resourceSetName,

            ImmutableArray<Outputs.ReadinessCheckTag> tags)
        {
            ReadinessCheckArn = readinessCheckArn;
            ResourceSetName = resourceSetName;
            Tags = tags;
        }
    }
}
