// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NimbleStudio.Inputs
{

    /// <summary>
    /// &lt;p&gt;An LDAP attribute of an Active Directory computer account, in the form of a name:value pair.&lt;/p&gt;
    /// </summary>
    public sealed class StudioComponentActiveDirectoryComputerAttributeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// &lt;p&gt;The name for the LDAP attribute.&lt;/p&gt;
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// &lt;p&gt;The value for the LDAP attribute.&lt;/p&gt;
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public StudioComponentActiveDirectoryComputerAttributeArgs()
        {
        }
        public static new StudioComponentActiveDirectoryComputerAttributeArgs Empty => new StudioComponentActiveDirectoryComputerAttributeArgs();
    }
}
