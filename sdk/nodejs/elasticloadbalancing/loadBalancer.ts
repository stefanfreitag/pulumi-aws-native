// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElasticLoadBalancing::LoadBalancer
 *
 * @deprecated LoadBalancer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class LoadBalancer extends pulumi.CustomResource {
    /**
     * Get an existing LoadBalancer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): LoadBalancer {
        pulumi.log.warn("LoadBalancer is deprecated: LoadBalancer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new LoadBalancer(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:elasticloadbalancing:LoadBalancer';

    /**
     * Returns true if the given object is an instance of LoadBalancer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LoadBalancer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LoadBalancer.__pulumiType;
    }

    public readonly accessLoggingPolicy!: pulumi.Output<outputs.elasticloadbalancing.LoadBalancerAccessLoggingPolicy | undefined>;
    public readonly appCookieStickinessPolicy!: pulumi.Output<outputs.elasticloadbalancing.LoadBalancerAppCookieStickinessPolicy[] | undefined>;
    public readonly availabilityZones!: pulumi.Output<string[] | undefined>;
    public /*out*/ readonly canonicalHostedZoneName!: pulumi.Output<string>;
    public /*out*/ readonly canonicalHostedZoneNameId!: pulumi.Output<string>;
    public readonly connectionDrainingPolicy!: pulumi.Output<outputs.elasticloadbalancing.LoadBalancerConnectionDrainingPolicy | undefined>;
    public readonly connectionSettings!: pulumi.Output<outputs.elasticloadbalancing.LoadBalancerConnectionSettings | undefined>;
    public readonly crossZone!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly dnsName!: pulumi.Output<string>;
    public readonly healthCheck!: pulumi.Output<outputs.elasticloadbalancing.LoadBalancerHealthCheck | undefined>;
    public readonly instances!: pulumi.Output<string[] | undefined>;
    public readonly lbCookieStickinessPolicy!: pulumi.Output<outputs.elasticloadbalancing.LoadBalancerLbCookieStickinessPolicy[] | undefined>;
    public readonly listeners!: pulumi.Output<outputs.elasticloadbalancing.LoadBalancerListeners[]>;
    public readonly loadBalancerName!: pulumi.Output<string | undefined>;
    public readonly policies!: pulumi.Output<outputs.elasticloadbalancing.LoadBalancerPolicies[] | undefined>;
    public readonly scheme!: pulumi.Output<string | undefined>;
    public readonly securityGroups!: pulumi.Output<string[] | undefined>;
    public readonly sourceSecurityGroupGroupName!: pulumi.Output<string | undefined>;
    public readonly sourceSecurityGroupOwnerAlias!: pulumi.Output<string | undefined>;
    public readonly subnets!: pulumi.Output<string[] | undefined>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a LoadBalancer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated LoadBalancer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: LoadBalancerArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("LoadBalancer is deprecated: LoadBalancer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.listeners === undefined) && !opts.urn) {
                throw new Error("Missing required property 'listeners'");
            }
            resourceInputs["accessLoggingPolicy"] = args ? args.accessLoggingPolicy : undefined;
            resourceInputs["appCookieStickinessPolicy"] = args ? args.appCookieStickinessPolicy : undefined;
            resourceInputs["availabilityZones"] = args ? args.availabilityZones : undefined;
            resourceInputs["connectionDrainingPolicy"] = args ? args.connectionDrainingPolicy : undefined;
            resourceInputs["connectionSettings"] = args ? args.connectionSettings : undefined;
            resourceInputs["crossZone"] = args ? args.crossZone : undefined;
            resourceInputs["healthCheck"] = args ? args.healthCheck : undefined;
            resourceInputs["instances"] = args ? args.instances : undefined;
            resourceInputs["lbCookieStickinessPolicy"] = args ? args.lbCookieStickinessPolicy : undefined;
            resourceInputs["listeners"] = args ? args.listeners : undefined;
            resourceInputs["loadBalancerName"] = args ? args.loadBalancerName : undefined;
            resourceInputs["policies"] = args ? args.policies : undefined;
            resourceInputs["scheme"] = args ? args.scheme : undefined;
            resourceInputs["securityGroups"] = args ? args.securityGroups : undefined;
            resourceInputs["sourceSecurityGroupGroupName"] = args ? args.sourceSecurityGroupGroupName : undefined;
            resourceInputs["sourceSecurityGroupOwnerAlias"] = args ? args.sourceSecurityGroupOwnerAlias : undefined;
            resourceInputs["subnets"] = args ? args.subnets : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["canonicalHostedZoneName"] = undefined /*out*/;
            resourceInputs["canonicalHostedZoneNameId"] = undefined /*out*/;
            resourceInputs["dnsName"] = undefined /*out*/;
        } else {
            resourceInputs["accessLoggingPolicy"] = undefined /*out*/;
            resourceInputs["appCookieStickinessPolicy"] = undefined /*out*/;
            resourceInputs["availabilityZones"] = undefined /*out*/;
            resourceInputs["canonicalHostedZoneName"] = undefined /*out*/;
            resourceInputs["canonicalHostedZoneNameId"] = undefined /*out*/;
            resourceInputs["connectionDrainingPolicy"] = undefined /*out*/;
            resourceInputs["connectionSettings"] = undefined /*out*/;
            resourceInputs["crossZone"] = undefined /*out*/;
            resourceInputs["dnsName"] = undefined /*out*/;
            resourceInputs["healthCheck"] = undefined /*out*/;
            resourceInputs["instances"] = undefined /*out*/;
            resourceInputs["lbCookieStickinessPolicy"] = undefined /*out*/;
            resourceInputs["listeners"] = undefined /*out*/;
            resourceInputs["loadBalancerName"] = undefined /*out*/;
            resourceInputs["policies"] = undefined /*out*/;
            resourceInputs["scheme"] = undefined /*out*/;
            resourceInputs["securityGroups"] = undefined /*out*/;
            resourceInputs["sourceSecurityGroupGroupName"] = undefined /*out*/;
            resourceInputs["sourceSecurityGroupOwnerAlias"] = undefined /*out*/;
            resourceInputs["subnets"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["loadBalancerName", "scheme"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(LoadBalancer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a LoadBalancer resource.
 */
export interface LoadBalancerArgs {
    accessLoggingPolicy?: pulumi.Input<inputs.elasticloadbalancing.LoadBalancerAccessLoggingPolicyArgs>;
    appCookieStickinessPolicy?: pulumi.Input<pulumi.Input<inputs.elasticloadbalancing.LoadBalancerAppCookieStickinessPolicyArgs>[]>;
    availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
    connectionDrainingPolicy?: pulumi.Input<inputs.elasticloadbalancing.LoadBalancerConnectionDrainingPolicyArgs>;
    connectionSettings?: pulumi.Input<inputs.elasticloadbalancing.LoadBalancerConnectionSettingsArgs>;
    crossZone?: pulumi.Input<boolean>;
    healthCheck?: pulumi.Input<inputs.elasticloadbalancing.LoadBalancerHealthCheckArgs>;
    instances?: pulumi.Input<pulumi.Input<string>[]>;
    lbCookieStickinessPolicy?: pulumi.Input<pulumi.Input<inputs.elasticloadbalancing.LoadBalancerLbCookieStickinessPolicyArgs>[]>;
    listeners: pulumi.Input<pulumi.Input<inputs.elasticloadbalancing.LoadBalancerListenersArgs>[]>;
    loadBalancerName?: pulumi.Input<string>;
    policies?: pulumi.Input<pulumi.Input<inputs.elasticloadbalancing.LoadBalancerPoliciesArgs>[]>;
    scheme?: pulumi.Input<string>;
    securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
    sourceSecurityGroupGroupName?: pulumi.Input<string>;
    sourceSecurityGroupOwnerAlias?: pulumi.Input<string>;
    subnets?: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
