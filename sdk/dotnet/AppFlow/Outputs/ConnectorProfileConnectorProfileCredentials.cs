// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Outputs
{

    /// <summary>
    /// Connector specific configuration needed to create connector profile based on Authentication mechanism
    /// </summary>
    [OutputType]
    public sealed class ConnectorProfileConnectorProfileCredentials
    {
        public readonly Outputs.ConnectorProfileAmplitudeConnectorProfileCredentials? Amplitude;
        public readonly Outputs.ConnectorProfileDatadogConnectorProfileCredentials? Datadog;
        public readonly Outputs.ConnectorProfileDynatraceConnectorProfileCredentials? Dynatrace;
        public readonly Outputs.ConnectorProfileGoogleAnalyticsConnectorProfileCredentials? GoogleAnalytics;
        public readonly Outputs.ConnectorProfileInforNexusConnectorProfileCredentials? InforNexus;
        public readonly Outputs.ConnectorProfileMarketoConnectorProfileCredentials? Marketo;
        public readonly Outputs.ConnectorProfileRedshiftConnectorProfileCredentials? Redshift;
        public readonly Outputs.ConnectorProfileSalesforceConnectorProfileCredentials? Salesforce;
        public readonly Outputs.ConnectorProfileServiceNowConnectorProfileCredentials? ServiceNow;
        public readonly Outputs.ConnectorProfileSingularConnectorProfileCredentials? Singular;
        public readonly Outputs.ConnectorProfileSlackConnectorProfileCredentials? Slack;
        public readonly Outputs.ConnectorProfileSnowflakeConnectorProfileCredentials? Snowflake;
        public readonly Outputs.ConnectorProfileTrendmicroConnectorProfileCredentials? Trendmicro;
        public readonly Outputs.ConnectorProfileVeevaConnectorProfileCredentials? Veeva;
        public readonly Outputs.ConnectorProfileZendeskConnectorProfileCredentials? Zendesk;

        [OutputConstructor]
        private ConnectorProfileConnectorProfileCredentials(
            Outputs.ConnectorProfileAmplitudeConnectorProfileCredentials? amplitude,

            Outputs.ConnectorProfileDatadogConnectorProfileCredentials? datadog,

            Outputs.ConnectorProfileDynatraceConnectorProfileCredentials? dynatrace,

            Outputs.ConnectorProfileGoogleAnalyticsConnectorProfileCredentials? googleAnalytics,

            Outputs.ConnectorProfileInforNexusConnectorProfileCredentials? inforNexus,

            Outputs.ConnectorProfileMarketoConnectorProfileCredentials? marketo,

            Outputs.ConnectorProfileRedshiftConnectorProfileCredentials? redshift,

            Outputs.ConnectorProfileSalesforceConnectorProfileCredentials? salesforce,

            Outputs.ConnectorProfileServiceNowConnectorProfileCredentials? serviceNow,

            Outputs.ConnectorProfileSingularConnectorProfileCredentials? singular,

            Outputs.ConnectorProfileSlackConnectorProfileCredentials? slack,

            Outputs.ConnectorProfileSnowflakeConnectorProfileCredentials? snowflake,

            Outputs.ConnectorProfileTrendmicroConnectorProfileCredentials? trendmicro,

            Outputs.ConnectorProfileVeevaConnectorProfileCredentials? veeva,

            Outputs.ConnectorProfileZendeskConnectorProfileCredentials? zendesk)
        {
            Amplitude = amplitude;
            Datadog = datadog;
            Dynatrace = dynatrace;
            GoogleAnalytics = googleAnalytics;
            InforNexus = inforNexus;
            Marketo = marketo;
            Redshift = redshift;
            Salesforce = salesforce;
            ServiceNow = serviceNow;
            Singular = singular;
            Slack = slack;
            Snowflake = snowflake;
            Trendmicro = trendmicro;
            Veeva = veeva;
            Zendesk = zendesk;
        }
    }
}
