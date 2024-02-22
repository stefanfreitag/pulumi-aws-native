// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Create and manage a Domain Configuration
 */
export class DomainConfiguration extends pulumi.CustomResource {
    /**
     * Get an existing DomainConfiguration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DomainConfiguration {
        return new DomainConfiguration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iot:DomainConfiguration';

    /**
     * Returns true if the given object is an instance of DomainConfiguration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DomainConfiguration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DomainConfiguration.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly authorizerConfig!: pulumi.Output<outputs.iot.DomainConfigurationAuthorizerConfig | undefined>;
    public readonly domainConfigurationName!: pulumi.Output<string | undefined>;
    public readonly domainConfigurationStatus!: pulumi.Output<enums.iot.DomainConfigurationStatus | undefined>;
    public readonly domainName!: pulumi.Output<string | undefined>;
    public /*out*/ readonly domainType!: pulumi.Output<enums.iot.DomainConfigurationDomainType>;
    public readonly serverCertificateArns!: pulumi.Output<string[] | undefined>;
    public readonly serverCertificateConfig!: pulumi.Output<outputs.iot.DomainConfigurationServerCertificateConfig | undefined>;
    public /*out*/ readonly serverCertificates!: pulumi.Output<outputs.iot.DomainConfigurationServerCertificateSummary[]>;
    public readonly serviceType!: pulumi.Output<enums.iot.DomainConfigurationServiceType | undefined>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;
    public readonly tlsConfig!: pulumi.Output<outputs.iot.DomainConfigurationTlsConfig | undefined>;
    public readonly validationCertificateArn!: pulumi.Output<string | undefined>;

    /**
     * Create a DomainConfiguration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DomainConfigurationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["authorizerConfig"] = args ? args.authorizerConfig : undefined;
            resourceInputs["domainConfigurationName"] = args ? args.domainConfigurationName : undefined;
            resourceInputs["domainConfigurationStatus"] = args ? args.domainConfigurationStatus : undefined;
            resourceInputs["domainName"] = args ? args.domainName : undefined;
            resourceInputs["serverCertificateArns"] = args ? args.serverCertificateArns : undefined;
            resourceInputs["serverCertificateConfig"] = args ? args.serverCertificateConfig : undefined;
            resourceInputs["serviceType"] = args ? args.serviceType : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["tlsConfig"] = args ? args.tlsConfig : undefined;
            resourceInputs["validationCertificateArn"] = args ? args.validationCertificateArn : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["domainType"] = undefined /*out*/;
            resourceInputs["serverCertificates"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["authorizerConfig"] = undefined /*out*/;
            resourceInputs["domainConfigurationName"] = undefined /*out*/;
            resourceInputs["domainConfigurationStatus"] = undefined /*out*/;
            resourceInputs["domainName"] = undefined /*out*/;
            resourceInputs["domainType"] = undefined /*out*/;
            resourceInputs["serverCertificateArns"] = undefined /*out*/;
            resourceInputs["serverCertificateConfig"] = undefined /*out*/;
            resourceInputs["serverCertificates"] = undefined /*out*/;
            resourceInputs["serviceType"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["tlsConfig"] = undefined /*out*/;
            resourceInputs["validationCertificateArn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["domainConfigurationName", "domainName", "serverCertificateArns[*]", "serviceType", "validationCertificateArn"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(DomainConfiguration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DomainConfiguration resource.
 */
export interface DomainConfigurationArgs {
    authorizerConfig?: pulumi.Input<inputs.iot.DomainConfigurationAuthorizerConfigArgs>;
    domainConfigurationName?: pulumi.Input<string>;
    domainConfigurationStatus?: pulumi.Input<enums.iot.DomainConfigurationStatus>;
    domainName?: pulumi.Input<string>;
    serverCertificateArns?: pulumi.Input<pulumi.Input<string>[]>;
    serverCertificateConfig?: pulumi.Input<inputs.iot.DomainConfigurationServerCertificateConfigArgs>;
    serviceType?: pulumi.Input<enums.iot.DomainConfigurationServiceType>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
    tlsConfig?: pulumi.Input<inputs.iot.DomainConfigurationTlsConfigArgs>;
    validationCertificateArn?: pulumi.Input<string>;
}
