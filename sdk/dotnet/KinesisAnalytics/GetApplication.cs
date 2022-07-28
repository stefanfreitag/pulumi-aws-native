// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalytics
{
    public static class GetApplication
    {
        /// <summary>
        /// Resource Type definition for AWS::KinesisAnalytics::Application
        /// </summary>
        public static Task<GetApplicationResult> InvokeAsync(GetApplicationArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetApplicationResult>("aws-native:kinesisanalytics:getApplication", args ?? new GetApplicationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::KinesisAnalytics::Application
        /// </summary>
        public static Output<GetApplicationResult> Invoke(GetApplicationInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetApplicationResult>("aws-native:kinesisanalytics:getApplication", args ?? new GetApplicationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetApplicationArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetApplicationArgs()
        {
        }
        public static new GetApplicationArgs Empty => new GetApplicationArgs();
    }

    public sealed class GetApplicationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetApplicationInvokeArgs()
        {
        }
        public static new GetApplicationInvokeArgs Empty => new GetApplicationInvokeArgs();
    }


    [OutputType]
    public sealed class GetApplicationResult
    {
        public readonly string? ApplicationCode;
        public readonly string? ApplicationDescription;
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.ApplicationInput> Inputs;

        [OutputConstructor]
        private GetApplicationResult(
            string? applicationCode,

            string? applicationDescription,

            string? id,

            ImmutableArray<Outputs.ApplicationInput> inputs)
        {
            ApplicationCode = applicationCode;
            ApplicationDescription = applicationDescription;
            Id = id;
            Inputs = inputs;
        }
    }
}
