// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetHub
{
    public static class GetApplication
    {
        /// <summary>
        /// Resource schema for AWS::IoTFleetHub::Application
        /// </summary>
        public static Task<GetApplicationResult> InvokeAsync(GetApplicationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetApplicationResult>("aws-native:iotfleethub:getApplication", args ?? new GetApplicationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::IoTFleetHub::Application
        /// </summary>
        public static Output<GetApplicationResult> Invoke(GetApplicationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetApplicationResult>("aws-native:iotfleethub:getApplication", args ?? new GetApplicationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetApplicationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the application.
        /// </summary>
        [Input("applicationId", required: true)]
        public string ApplicationId { get; set; } = null!;

        public GetApplicationArgs()
        {
        }
        public static new GetApplicationArgs Empty => new GetApplicationArgs();
    }

    public sealed class GetApplicationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the application.
        /// </summary>
        [Input("applicationId", required: true)]
        public Input<string> ApplicationId { get; set; } = null!;

        public GetApplicationInvokeArgs()
        {
        }
        public static new GetApplicationInvokeArgs Empty => new GetApplicationInvokeArgs();
    }


    [OutputType]
    public sealed class GetApplicationResult
    {
        /// <summary>
        /// The ARN of the application.
        /// </summary>
        public readonly string? ApplicationArn;
        /// <summary>
        /// When the Application was created
        /// </summary>
        public readonly int? ApplicationCreationDate;
        /// <summary>
        /// Application Description, should be between 1 and 2048 characters.
        /// </summary>
        public readonly string? ApplicationDescription;
        /// <summary>
        /// The ID of the application.
        /// </summary>
        public readonly string? ApplicationId;
        /// <summary>
        /// When the Application was last updated
        /// </summary>
        public readonly int? ApplicationLastUpdateDate;
        /// <summary>
        /// Application Name, should be between 1 and 256 characters.
        /// </summary>
        public readonly string? ApplicationName;
        /// <summary>
        /// The current state of the application.
        /// </summary>
        public readonly string? ApplicationState;
        /// <summary>
        /// The URL of the application.
        /// </summary>
        public readonly string? ApplicationUrl;
        /// <summary>
        /// A message indicating why Create or Delete Application failed.
        /// </summary>
        public readonly string? ErrorMessage;
        /// <summary>
        /// The ARN of the role that the web application assumes when it interacts with AWS IoT Core. For more info on configuring this attribute, see https://docs.aws.amazon.com/iot/latest/apireference/API_iotfleethub_CreateApplication.html#API_iotfleethub_CreateApplication_RequestSyntax
        /// </summary>
        public readonly string? RoleArn;
        /// <summary>
        /// The AWS SSO application generated client ID (used with AWS SSO APIs).
        /// </summary>
        public readonly string? SsoClientId;
        /// <summary>
        /// A list of key-value pairs that contain metadata for the application.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetApplicationResult(
            string? applicationArn,

            int? applicationCreationDate,

            string? applicationDescription,

            string? applicationId,

            int? applicationLastUpdateDate,

            string? applicationName,

            string? applicationState,

            string? applicationUrl,

            string? errorMessage,

            string? roleArn,

            string? ssoClientId,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            ApplicationArn = applicationArn;
            ApplicationCreationDate = applicationCreationDate;
            ApplicationDescription = applicationDescription;
            ApplicationId = applicationId;
            ApplicationLastUpdateDate = applicationLastUpdateDate;
            ApplicationName = applicationName;
            ApplicationState = applicationState;
            ApplicationUrl = applicationUrl;
            ErrorMessage = errorMessage;
            RoleArn = roleArn;
            SsoClientId = ssoClientId;
            Tags = tags;
        }
    }
}
