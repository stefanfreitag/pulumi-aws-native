// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    /// <summary>
    /// &lt;p&gt;Data source credentials. This is a variant type structure. For this structure to be
    ///             valid, only one of the attributes can be non-null.&lt;/p&gt;
    /// </summary>
    public sealed class DataSourceCredentialsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// &lt;p&gt;The Amazon Resource Name (ARN) of a data source that has the credential pair that you
        ///             want to use. When &lt;code&gt;CopySourceArn&lt;/code&gt; is not null, the credential pair from the
        ///             data source in the ARN is used as the credentials for the
        ///             &lt;code&gt;DataSourceCredentials&lt;/code&gt; structure.&lt;/p&gt;
        /// </summary>
        [Input("copySourceArn")]
        public Input<string>? CopySourceArn { get; set; }

        [Input("credentialPair")]
        public Input<Inputs.DataSourceCredentialPairArgs>? CredentialPair { get; set; }

        public DataSourceCredentialsArgs()
        {
        }
        public static new DataSourceCredentialsArgs Empty => new DataSourceCredentialsArgs();
    }
}
