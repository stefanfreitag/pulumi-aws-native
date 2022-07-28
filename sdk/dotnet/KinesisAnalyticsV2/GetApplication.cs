// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalyticsV2
{
    public static class GetApplication
    {
        /// <summary>
        /// Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see [Creating an Application](https://docs.aws.amazon.com/kinesisanalytics/latest/java/getting-started.html).
        /// </summary>
        public static Task<GetApplicationResult> InvokeAsync(GetApplicationArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetApplicationResult>("aws-native:kinesisanalyticsv2:getApplication", args ?? new GetApplicationArgs(), options.WithDefaults());

        /// <summary>
        /// Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see [Creating an Application](https://docs.aws.amazon.com/kinesisanalytics/latest/java/getting-started.html).
        /// </summary>
        public static Output<GetApplicationResult> Invoke(GetApplicationInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetApplicationResult>("aws-native:kinesisanalyticsv2:getApplication", args ?? new GetApplicationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetApplicationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the application.
        /// </summary>
        [Input("applicationName", required: true)]
        public string ApplicationName { get; set; } = null!;

        public GetApplicationArgs()
        {
        }
        public static new GetApplicationArgs Empty => new GetApplicationArgs();
    }

    public sealed class GetApplicationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the application.
        /// </summary>
        [Input("applicationName", required: true)]
        public Input<string> ApplicationName { get; set; } = null!;

        public GetApplicationInvokeArgs()
        {
        }
        public static new GetApplicationInvokeArgs Empty => new GetApplicationInvokeArgs();
    }


    [OutputType]
    public sealed class GetApplicationResult
    {
        /// <summary>
        /// Use this parameter to configure the application.
        /// </summary>
        public readonly Outputs.ApplicationConfiguration? ApplicationConfiguration;
        /// <summary>
        /// The description of the application.
        /// </summary>
        public readonly string? ApplicationDescription;
        /// <summary>
        /// Specifies the IAM role that the application uses to access external resources.
        /// </summary>
        public readonly string? ServiceExecutionRole;
        /// <summary>
        /// A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.
        /// </summary>
        public readonly ImmutableArray<Outputs.ApplicationTag> Tags;

        [OutputConstructor]
        private GetApplicationResult(
            Outputs.ApplicationConfiguration? applicationConfiguration,

            string? applicationDescription,

            string? serviceExecutionRole,

            ImmutableArray<Outputs.ApplicationTag> tags)
        {
            ApplicationConfiguration = applicationConfiguration;
            ApplicationDescription = applicationDescription;
            ServiceExecutionRole = serviceExecutionRole;
            Tags = tags;
        }
    }
}
