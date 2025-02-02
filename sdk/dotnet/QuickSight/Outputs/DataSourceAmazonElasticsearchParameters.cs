// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    /// <summary>
    /// &lt;p&gt;Amazon Elasticsearch Service parameters.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class DataSourceAmazonElasticsearchParameters
    {
        /// <summary>
        /// &lt;p&gt;The Amazon Elasticsearch Service domain.&lt;/p&gt;
        /// </summary>
        public readonly string Domain;

        [OutputConstructor]
        private DataSourceAmazonElasticsearchParameters(string domain)
        {
            Domain = domain;
        }
    }
}
