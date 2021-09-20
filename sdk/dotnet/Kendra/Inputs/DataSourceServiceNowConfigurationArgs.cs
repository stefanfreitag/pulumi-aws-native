// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Inputs
{

    public sealed class DataSourceServiceNowConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("hostUrl", required: true)]
        public Input<string> HostUrl { get; set; } = null!;

        [Input("knowledgeArticleConfiguration")]
        public Input<Inputs.DataSourceServiceNowKnowledgeArticleConfigurationArgs>? KnowledgeArticleConfiguration { get; set; }

        [Input("secretArn", required: true)]
        public Input<string> SecretArn { get; set; } = null!;

        [Input("serviceCatalogConfiguration")]
        public Input<Inputs.DataSourceServiceNowServiceCatalogConfigurationArgs>? ServiceCatalogConfiguration { get; set; }

        [Input("serviceNowBuildVersion", required: true)]
        public Input<Pulumi.AwsNative.Kendra.DataSourceServiceNowBuildVersionType> ServiceNowBuildVersion { get; set; } = null!;

        public DataSourceServiceNowConfigurationArgs()
        {
        }
    }
}
