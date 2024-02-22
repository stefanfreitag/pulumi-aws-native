// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SystemsManagerSap
{
    public static class GetApplication
    {
        /// <summary>
        /// Resource schema for AWS::SystemsManagerSAP::Application
        /// </summary>
        public static Task<GetApplicationResult> InvokeAsync(GetApplicationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetApplicationResult>("aws-native:systemsmanagersap:getApplication", args ?? new GetApplicationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::SystemsManagerSAP::Application
        /// </summary>
        public static Output<GetApplicationResult> Invoke(GetApplicationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetApplicationResult>("aws-native:systemsmanagersap:getApplication", args ?? new GetApplicationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetApplicationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the Helix application
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetApplicationArgs()
        {
        }
        public static new GetApplicationArgs Empty => new GetApplicationArgs();
    }

    public sealed class GetApplicationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the Helix application
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetApplicationInvokeArgs()
        {
        }
        public static new GetApplicationInvokeArgs Empty => new GetApplicationInvokeArgs();
    }


    [OutputType]
    public sealed class GetApplicationResult
    {
        public readonly string? ApplicationId;
        public readonly Pulumi.AwsNative.SystemsManagerSap.ApplicationType? ApplicationType;
        /// <summary>
        /// The ARN of the Helix application
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The tags of a SystemsManagerSAP application.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetApplicationResult(
            string? applicationId,

            Pulumi.AwsNative.SystemsManagerSap.ApplicationType? applicationType,

            string? arn,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            ApplicationId = applicationId;
            ApplicationType = applicationType;
            Arn = arn;
            Tags = tags;
        }
    }
}
