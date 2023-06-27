// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApplicationInsights
{
    public static class GetApplication
    {
        /// <summary>
        /// Resource schema for AWS::ApplicationInsights::Application
        /// </summary>
        public static Task<GetApplicationResult> InvokeAsync(GetApplicationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetApplicationResult>("aws-native:applicationinsights:getApplication", args ?? new GetApplicationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::ApplicationInsights::Application
        /// </summary>
        public static Output<GetApplicationResult> Invoke(GetApplicationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetApplicationResult>("aws-native:applicationinsights:getApplication", args ?? new GetApplicationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetApplicationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the ApplicationInsights application.
        /// </summary>
        [Input("applicationARN", required: true)]
        public string ApplicationARN { get; set; } = null!;

        public GetApplicationArgs()
        {
        }
        public static new GetApplicationArgs Empty => new GetApplicationArgs();
    }

    public sealed class GetApplicationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the ApplicationInsights application.
        /// </summary>
        [Input("applicationARN", required: true)]
        public Input<string> ApplicationARN { get; set; } = null!;

        public GetApplicationInvokeArgs()
        {
        }
        public static new GetApplicationInvokeArgs Empty => new GetApplicationInvokeArgs();
    }


    [OutputType]
    public sealed class GetApplicationResult
    {
        /// <summary>
        /// The ARN of the ApplicationInsights application.
        /// </summary>
        public readonly string? ApplicationARN;
        /// <summary>
        /// If set to true, application will be configured with recommended monitoring configuration.
        /// </summary>
        public readonly bool? AutoConfigurationEnabled;
        /// <summary>
        /// Indicates whether Application Insights can listen to CloudWatch events for the application resources.
        /// </summary>
        public readonly bool? CWEMonitorEnabled;
        /// <summary>
        /// The monitoring settings of the components.
        /// </summary>
        public readonly ImmutableArray<Outputs.ApplicationComponentMonitoringSetting> ComponentMonitoringSettings;
        /// <summary>
        /// The custom grouped components.
        /// </summary>
        public readonly ImmutableArray<Outputs.ApplicationCustomComponent> CustomComponents;
        /// <summary>
        /// The grouping type of the application
        /// </summary>
        public readonly Pulumi.AwsNative.ApplicationInsights.ApplicationGroupingType? GroupingType;
        /// <summary>
        /// The log pattern sets.
        /// </summary>
        public readonly ImmutableArray<Outputs.ApplicationLogPatternSet> LogPatternSets;
        /// <summary>
        /// When set to true, creates opsItems for any problems detected on an application.
        /// </summary>
        public readonly bool? OpsCenterEnabled;
        /// <summary>
        /// The SNS topic provided to Application Insights that is associated to the created opsItem.
        /// </summary>
        public readonly string? OpsItemSNSTopicArn;
        /// <summary>
        /// The tags of Application Insights application.
        /// </summary>
        public readonly ImmutableArray<Outputs.ApplicationTag> Tags;

        [OutputConstructor]
        private GetApplicationResult(
            string? applicationARN,

            bool? autoConfigurationEnabled,

            bool? cWEMonitorEnabled,

            ImmutableArray<Outputs.ApplicationComponentMonitoringSetting> componentMonitoringSettings,

            ImmutableArray<Outputs.ApplicationCustomComponent> customComponents,

            Pulumi.AwsNative.ApplicationInsights.ApplicationGroupingType? groupingType,

            ImmutableArray<Outputs.ApplicationLogPatternSet> logPatternSets,

            bool? opsCenterEnabled,

            string? opsItemSNSTopicArn,

            ImmutableArray<Outputs.ApplicationTag> tags)
        {
            ApplicationARN = applicationARN;
            AutoConfigurationEnabled = autoConfigurationEnabled;
            CWEMonitorEnabled = cWEMonitorEnabled;
            ComponentMonitoringSettings = componentMonitoringSettings;
            CustomComponents = customComponents;
            GroupingType = groupingType;
            LogPatternSets = logPatternSets;
            OpsCenterEnabled = opsCenterEnabled;
            OpsItemSNSTopicArn = opsItemSNSTopicArn;
            Tags = tags;
        }
    }
}
